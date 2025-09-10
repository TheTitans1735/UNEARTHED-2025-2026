# -*- coding: utf-8 -*-
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor,ForceSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Stop, Icon, Color, Button, Direction
from pybricks.tools import wait, StopWatch
from pybricks.iodevices import XboxController

class RollExceededException(Exception):
    pass
class over_roll(Exception):
    pass


class PIDController:
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
    def wrapper(*args, **kwargs):
        timer = StopWatch()
        result = func(*args, **kwargs)
        run_took = timer.time() / 1000.0
        print(f"run took {run_took} sec")
        return result
    return wrapper


class color:
    BLACK = "black"
    GRAY = "gray"
    BLUE = "blue"
    LIGHT_BLUE = "light_blue"
    LIGHT_GREEN = "light_green"
    LIGHT_PURPLE = "light_purple"
    ORANGE = "orange"
    MUSTARD = "mustard"
    UNKNOWN = "unknown"

    GRAY = "gray"
    @staticmethod
    def detect(self, h, s, v):
        if v < 15:
            return color.BLACK
        

        if 180 <= h <= 210 and s > 40 and v > 60:
            return color.LIGHT_BLUE
        elif 210 <= h <= 250 and s > 40:
            return color.BLUE

        elif 70 <= h <= 95 and s > 40 and v > 60:
            return color.LIGHT_GREEN

        elif 260 <= h <= 290 and s > 30 and v > 60:
            return color.LIGHT_PURPLE

        elif 20 <= h <= 35 and s > 50 and v > 50:
            return color.ORANGE

        elif 40 <= h <= 60 and s > 50 and v > 50:
            return color.MUSTARD

        return color.UNKNOWN

class Robot:
    def __init__(self):
        self.hub = PrimeHub()
        self.left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.D)
        self.motor_front = Motor(Port.E)
        self.motor_back = Motor(Port.A)
        self.drive_base = DriveBase(self.left_motor, self.right_motor, 62.4, 120)
        # self.color_sensor = ColorSensor(Port.C)
        self.force_sensor = ForceSensor(port=Port.B)
        self.drive_base.use_gyro(True)
        self.emergency_stop = False
        self.color_sensor = ColorSensor(Port.C)


# נוסע כל הזמן עד שמזהה צבע קסטום (לא UNKNOWN)

    async def battery_status(self):
        voltage = self.hub.battery.voltage()
        print(f"{voltage=}")
        if voltage > 8000:
            self.hub.light.blink(Color.GREEN, [1000])
        elif voltage > 7500:
            self.hub.light.blink(Color.BLUE, [1000])
        elif voltage > 7000:
            self.hub.light.blink(Color.ORANGE, [1000])
        else:
            self.hub.light.blink(Color.RED, [1000])

    async def run_front_motor(self, speed, angle, wait=True):
        speed = 110
        self.motor_front.reset_angle(0)
        await self.motor_front.run_target(speed, angle, then=Stop.HOLD, wait=wait)

    async def run_back_motor(self, speed, angle, wait=True):
        self.motor_back.reset_angle(0)
        await self.motor_back.run_target(speed, angle, then=Stop.HOLD, wait=wait)

    async def wait_for_button(self, debug=True):
        if not debug:
            return
        self.hub.light.blink(Color.MAGENTA, [1000])
        while not self.hub.buttons.pressed():
            await wait(10)
        self.buttery_status()

    async def drive_straight(self, distance_cm,
                             target_speed=1000, 
                             stop_at_end=True,
                             gradual_stop=True,
                             gradtual_start=True):
        acceleration_rate = target_speed / 2 if gradtual_start else target_speed
        deceleration_rate = target_speed / 2 if gradual_stop else target_speed
        
        self.drive_base.settings(target_speed, (acceleration_rate, deceleration_rate), None, None)
        await self.drive_base.straight(distance_cm * 10, then=Stop.HOLD if stop_at_end else Stop.NONE, wait=True)
        self.left_motor.stop()
        self.right_motor.stop()
        self.hub.imu.reset_heading(0)

    async def drive_straight_with_pid_old(self, distance_cm, target_speed=300, stop_at_end=True, timeout_seconds=None, gradual_stop=True, gradtual_start=True, kp=1, ki=0, kd=0):
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

            if timeout_seconds is not None and timer.time() > timeout_seconds:
                break

            await wait(1)

        if stop_at_end:
            self.drive_base.stop()

    async def turn(self, degrees, speed=150):
        await wait(10)
        self.drive_base.stop()  # <-- Stop driving before resetting heading
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
        self.drive_base.stop()  # <-- Stop driving before resetting heading
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
        self.drive_base.reset()
        self.drive_base.settings(speed, None, None, None)
        await self.drive_base.curve(radius, angle, then, wait)

    # async def monitor_pitch(self):
    #     while True:
    #         pitch, roll = self.hub.imu.tilt()
    #         if abs(roll) >= 50:
    #             print("Roll above 50! Stopping robot and returning to menu.")
    #             self.drive_base.stop()
    #             self.motor_back.stop()
    #             self.motor_front.stop()
    #             return
    #         await wait(100)
    async def drive_until_button(self,speed=500):#speed_of_drive=500):
        # 
        self.drive_base.drive(speed, 0)
        while not await self.force_sensor.pressed():
            await wait(10)
        self.drive_base.stop()
        self.motor_front.stop()
        self.motor_back.stop()
    async def drive_until_touch(self,speed=500):#speed_of_drive=500):
        
        self.drive_base.drive(speed, 0)
        while not await self.force_sensor.touched():
            await wait(10)
        self.drive_base.stop()
        self.motor_front.stop()
        self.motor_back.stop()
    async def drive_until_bluetooth(self, speed=500):
        """
        מתחיל לנסוע קדימה, ואם לוחצים על כפתור BLUETOOTH עוצר וחוזר לתפריט.
        """
        self.drive_base.drive(speed, 0)
        while True:
            pressed = self.hub.buttons.pressed()
            if Button.BLUETOOTH in pressed:
                self.drive_base.stop()
                break
            await wait(50)

    async def run_until_force_press(self, speed=750):
        """
        Drives forward until the force sensor is pressed, then stops all motors.
        """
        self.drive_base.drive(speed, 0)
        while not self.forcesensor.pressed():
            await wait(10)
        self.drive_base.stop()
        self.motor_front.stop()
        self.motor_back.stop()



    async def print_force_sensor(self):
        """
        Prints the force sensor value every second.
        """
        while True:
            # Read all the information we can get from this sensor.
            force = self.force_sensor.force()
            dist = self.force_sensor.distance()
            press = self.force_sensor.pressed()
            touch = self.force_sensor.touched()

            # Print the values
            print("Force", force, "Dist:", dist, "Pressed:", press, "Touched:", touch)

            # Push the sensor button see what happens to the values.

            # Wait some time so we can read what is printed.
            await wait(200)
            
    async def run_until_force_press(self, speed=750):
        self.drive_base.drive(speed, 0)
        while not await self.force_sensor.pressed():
            await wait(10)
        self.drive_base.stop()
        self.motor_front.stop()
        self.motor_back.stop()
        
    async def run_until_force_touched(self, speed=750):
        self.drive_base.drive(speed, 0)
        while not await self.force_sensor.touched():
            await wait(10)
        self.drive_base.stop()
        self.motor_front.stop()
        self.motor_back.stop()
        
    # async def detect_color_and_run(self):
    #     while True:
    #         detected_color = await self.color_sensor.color()
    #         print(f"Detected: {detected_color}")
    