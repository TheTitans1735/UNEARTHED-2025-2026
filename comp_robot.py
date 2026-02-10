from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, ForceSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Stop, Icon, Color, Button, Direction
from pybricks.tools import wait, StopWatch
from pybricks.iodevices import XboxController


# ==================== Helper Classes ====================


class PIDController:
    """בקר PID לתיאום מהירות המנוע"""
    
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previous_error = 0
        self.integral = 0

    async def compute(self, target, current):
        error = target - current
        self.integral += error
        derivative = error - self.previous_error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        return output


def time_it(func):
    """דקורטור למדידת זמן ביצוע של פונקציה"""
    def wrapper(*args, **kwargs):
        timer = StopWatch()
        result = func(*args, **kwargs)
        run_took = timer.time() / 1000.0
        print(f"run took {run_took} sec")
        return result
    return wrapper


# ==================== Robot Class ====================


class Robot:
    """מחלקת הרובוט הראשית הטיפולה בכל פעולות המנועים וחיישנים"""

    # ==================== Initialization ====================

    def __init__(self):
        """אתחול רובוט, מנועים, חיישנים וגלגלים"""
        self.hub = PrimeHub()
        self.left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.D)
        self.motor_front = Motor(Port.E)
        self.motor_back = Motor(Port.A)
        self.drive_base = DriveBase(self.left_motor, self.right_motor, 62.4, 120)
        self.force_sensor = ForceSensor(port=Port.B)
        self.drive_base.use_gyro(True)
        self.emergency_stop = False
        self.color_sensor = ColorSensor(Port.C)
        self.color_sensor.detectable_colors([
            Color.BLACK, Color.BLUE, Color.RED,
            Color.ORANGE, Color.YELLOW, Color.GRAY, Color.WHITE, Color.NONE
        ])

    # ==================== Battery Status ====================

    async def battery_status(self):
        """בדוק מתח הסוללה והצג סטטוס דרך צבע האור של הקולט"""
        voltage = self.hub.battery.voltage()
        print(f"Battery voltage: {voltage}mV")
        if voltage > 8000:
            self.hub.light.blink(Color.GREEN, [1000])
        elif voltage > 7500:
            self.hub.light.blink(Color.BLUE, [1000])
        elif voltage > 7000:
            self.hub.light.blink(Color.ORANGE, [1000])
        else:
            self.hub.light.blink(Color.RED, [1000]) 

    # ==================== Front Motor Control ====================

    async def run_front_motor(self, speed=100, angle=90, wait=True):
        """הפעל מנוע קדמי לזווית מסוימת במהירות נתונה (מעלות/שנייה)"""
        self.motor_front.reset_angle(0)
        await self.motor_front.run_target(speed, angle, then=Stop.HOLD, wait=wait)

    async def run_front_motor_fast(self, duty=100, time_seconds=1.0, should_wait=True):
        """הפעל מנוע קדמי במהירות גבוהה עם מחזור זמן למשך זמן מסוים"""
        self.motor_front.dc(duty)
        if should_wait:
            await wait(time_seconds * 1000)
            self.motor_front.stop()

    # ==================== Back Motor Control ====================

    async def run_back_motor(self, speed, angle, wait=True):
        """הפעל מנוע אחורי לזווית מסוימת במהירות נתונה (מעלות/שנייה)"""
        self.motor_back.reset_angle(0)
        await self.motor_back.run_target(speed, angle, then=Stop.HOLD, wait=wait)

    async def run_back_motor_fast(self, duty=100, time_seconds=1.0, should_wait=True):
        """הפעל מנוע אחורי במהירות גבוהה עם מחזור זמן למשך זמן מסוים"""
        self.motor_back.dc(duty)
        if should_wait:
            await wait(time_seconds * 1000)
            self.motor_back.stop()


    # ==================== Basic Movement ====================

    async def wait_for_button(self, debug=True):
        """חכה ללחיצת כפתור על הקולט ובדוק סטטוס סוללה"""
        if not debug:
            return
        self.hub.light.blink(Color.MAGENTA, [1000])
        while not self.hub.buttons.pressed():
            await wait(10)
        await self.battery_status()

    async def drive_straight(self, distance_cm, target_speed=1000, stop_at_end=True,
                             gradual_stop=True, gradual_start=True):
        """נסע ישר למרחק מסוים עם תאוצה/האטה אופציונלית"""
        acceleration_rate = target_speed / 2 if gradual_start else target_speed
        deceleration_rate = target_speed / 2 if gradual_stop else target_speed
        
        self.drive_base.settings(target_speed, (acceleration_rate, deceleration_rate), None, None)
        await self.drive_base.straight(distance_cm * 10, then=Stop.HOLD if stop_at_end else Stop.NONE, wait=True)
        self.left_motor.stop()
        self.right_motor.stop()
        self.hub.imu.reset_heading(0)

    async def drive_straight2(self, distance_cm, target_speed=1000, stop_at_end=True,
                              gradual_stop=True, gradual_start=True):
        """נסע ישר למרחקים ארוכים יותר עם תאוצה/האטה עדינה יותר"""
        acceleration_rate = target_speed / 5 if gradual_start else target_speed
        deceleration_rate = target_speed / 4 if gradual_stop else target_speed
        
        self.drive_base.settings(target_speed, (acceleration_rate, deceleration_rate), None, None)
        await self.drive_base.straight(distance_cm * 10, then=Stop.HOLD if stop_at_end else Stop.NONE, wait=True)
        self.left_motor.stop()
        self.right_motor.stop()
        self.hub.imu.reset_heading(0)

  
    async def drive_straight_with_pid(self, distance_cm, target_speed=300, stop_at_end=True,
                                       timeout_seconds=None, gradual_stop=True, gradual_start=True,
                                       kp=1, ki=0, kd=0):
        """נסע ישר בשימוש בקר PID לתיקון ג'ירו"""
        pid = PIDController(kp, ki, kd)
        timer = StopWatch()
        target_distance = distance_cm * 10

        if distance_cm < 0:
            target_speed = -target_speed
            target_distance = -target_distance

        self.drive_base.reset()
        direction = 1 if distance_cm > 0 else -1

        while True:
            current_angle = self.drive_base.angle()
            current_distance = self.drive_base.distance()
            correction = await pid.compute(0, current_angle)

            if abs(current_distance) < target_distance / 2:
                speed = target_speed
            else:
                speed = target_speed
                if gradual_stop:
                    speed = target_speed * (target_distance - abs(current_distance)) / (target_distance / 2)

            if abs(speed) < 100:
                speed = 100 * direction

            print(f"Speed: {speed}, Correction: {correction}, travel: {current_distance}, current_angle: {current_angle}")
            self.drive_base.drive(speed, correction)

            if abs(current_distance) >= abs(target_distance):
                break

            if timeout_seconds is not None and timer.time() > timeout_seconds * 1000:
                break

            await wait(1)

        if stop_at_end:
            self.drive_base.stop()

    # ==================== Turning ====================

    async def turn(self, degrees, speed=150):
        """סובב רובוט בשימוש שני הגלגלים (נסיעה דיפרנציאלית)"""
        await wait(10)
        self.drive_base.stop()
        self.hub.imu.reset_heading(0)
        if degrees > 0:
            self.left_motor.run(speed)
            self.right_motor.run(-speed)
        else:
            self.left_motor.run(-speed)
            self.right_motor.run(speed)

        while abs(self.hub.imu.heading() - degrees) > 2:
            await wait(0.1)

        self.left_motor.stop()
        self.right_motor.stop()

    async def turn_without_right_wheel(self, degrees, speed=150):
        """סובב רובוט בשימוש הגלגל השמאלי בלבד"""
        self.drive_base.stop()
        self.hub.imu.reset_heading(0)
        if degrees > 0:
            self.left_motor.run(speed)
        else:
            self.left_motor.run(-speed)

        while abs(self.hub.imu.heading() - degrees) > 2:
            await wait(0)

        self.left_motor.stop()
        self.right_motor.stop()

    async def curve(self, radius, angle, speed, then=Stop.HOLD, wait=True):
        """הזז רובוט בנתיב מעוקל"""
        self.drive_base.reset()
        self.drive_base.settings(speed, None, None, None)
        await self.drive_base.curve(radius, angle, then, wait)

    # ==================== Conditional Driving ====================

    async def drive_until_button(self, speed=500):
        """נסע עד שכפתור חיישן הכוח ללחוץ"""
        self.drive_base.drive(speed, 0)
        while not await self.force_sensor.pressed():
            await wait(10)
        self.drive_base.stop()
        self.motor_front.stop()
        self.motor_back.stop()

    async def drive_until_touch(self, speed=500):
        """נסע עד שחיישן הכוח נגוע"""
        self.drive_base.drive(speed, 0)
        while not await self.force_sensor.touched():
            await wait(10)
        self.drive_base.stop()
        self.motor_front.stop()
        self.motor_back.stop()

    async def drive_until_bluetooth(self, speed=500):
        """נסע קדימה עד שכפתור בלוטוס ללחוץ"""
        self.drive_base.drive(speed, 0)
        while True:
            pressed = self.hub.buttons.pressed()
            if Button.BLUETOOTH in pressed:
                self.drive_base.stop()
                break
            await wait(50)

    async def run_until_force_press(self, speed=750):
        """הפעל מנועים עד שחיישן הכוח ללחוץ"""
        self.drive_base.drive(speed, 0)
        while not await self.force_sensor.pressed():
            await wait(10)
        self.drive_base.stop()
        self.motor_front.stop()
        self.motor_back.stop()

    async def run_until_force_touched(self, speed=750, max_force=4.200):
        """הפעל עד שמרחק חיישן הכוח עולה על הסף"""
        self.drive_base.drive(speed, 0)
        if 0.800 < self.force_sensor.distance() < max_force:
            self.left_motor.stop()
            self.right_motor.stop()
            await wait(10)

    # ==================== Sensor Reading ====================

    async def print_force_sensor(self):
        """הדפס קריאות חיישן כוח ברציפות"""
        while True:
            force = self.force_sensor.force()
            dist = self.force_sensor.distance()
            press = await self.force_sensor.pressed()
            touch = await self.force_sensor.touched()

            print(f"Force: {force}, Distance: {dist}, Pressed: {press}, Touched: {touch}")
            await wait(200)