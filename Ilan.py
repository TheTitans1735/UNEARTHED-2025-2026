from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, ForceSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch, run_task, multitask
from pybricks.parameters import Icon, Color, Button, Direction
from robot import Robot,time_it,Stop, over_roll
ilan=Robot()

async def stop_all():
    """
    תכנית לעצירת כל המנועים.
    """
    ilan.drive_base.stop()
    ilan.motor_back.stop()
    ilan.motor_front.stop()
    
async def ritsatMaavar():
    debug=True
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(33, 750) # יציאה מהבית הכחול למשימה 8
    await ilan.wait_for_button(debug)
    
    await ilan.run_front_motor_fast(100, 3) # ביצוע משימה 8
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor(5000, -800)
    await ilan.wait_for_button(debug)

    await ilan.turn(-50) # הגעה ממשימה 8 למשימה 9
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(28,800)
    await ilan.wait_for_button(debug)
    await ilan.turn(-10)

    await ilan.wait_for_button(debug) # ביצוע משימה 9
    await ilan.run_back_motor(5000,800)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor(5000,-800)
    await ilan.wait_for_button(debug)
    await ilan.turn(-30)
    await ilan.wait_for_button(debug)
    await ilan.drive_until_touch()
    await ilan.wait_for_button(debug)
    await ilan.turn(-20)

    await ilan.wait_for_button(debug)
    await ilan.drive_straight(16,500) # הגעה ממשימה 9 למשימה 10

    await ilan.wait_for_button(debug) # ביצוע משימה 10
    await ilan.turn(80)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(5,200)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor(800,180)
    await ilan.wait_for_button(debug)
    await ilan.run_back_motor(-800,180)   

async def discover():
  await ilan.drive_straight(-40, 500)
  await ilan.turn(74)
  await ilan.drive_straight(75, 500)
  await ilan.turn(8)
  await ilan.turn(-24)
  await ilan.drive_straight(-7, 500)
  await ilan.turn(-9)
  await ilan.drive_straight
  # לא גמור

async def forum():
    debug=True
    await ilan.wait_for_button(debug)
    await ilan.turn(17, speed=150)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(71, 700)
    await ilan.wait_for_button(debug)
    await ilan.turn(58, speed=150)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(20, 700)
    await ilan.wait_for_button(debug)
    await ilan.turn(90, speed=150)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(10, 700)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor(700, -20)
    await ilan.wait_for_button(debug)
    await ilan.turn(-11, speed=150)
    await ilan.wait_for_button(debug)
    await ilan.run.front_motor(700, -70)

async def detect_color_and_run():
        print("Starting color detection...")
        #await forum()
        detected_color = await ilan.color_sensor.color()
        print(detected_color)
        await wait(100)

        if detected_color == Color.BLUE:
            ilan.hub.display.icon(Icon.TRIANGLE_LEFT)
            while True:
                if Button.BLUETOOTH in ilan.hub.buttons.pressed():
                    # כאן תפעיל פונקציה מתאימה
                    await ilan.drive_until_touched(speed=100)
                    break

        elif detected_color == Color.GRAY:
            ilan.hub.display.icon(Icon.SQUARE)
            while True:
                if Button.BLUETOOTH in ilan.hub.buttons.pressed():
                    await "funk()"
                    break
           
        elif detected_color == Color.YELLOW:
            ilan.hub.display.icon(Icon.SAD)
            while True:
                if Button.BLUETOOTH in ilan.hub.buttons.pressed():  
                    await "funk()"
                    break
        elif detected_color == Color.WHITE:
            ilan.hub.display.icon(Icon.EYE_RIGHT)
            while True:
                if Button.BLUETOOTH in ilan.hub.buttons.pressed():
                    await "funk()"
                    break

        elif detected_color == Color.RED:
            ilan.hub.display.icon(Icon.TRIANGLE_LEFT)
            while True:
                if Button.BLUETOOTH in ilan.hub.buttons.pressed():
                    await "funk()"
                    break



async def monitor_roll():
    roll_exceeded = False
    while True:
        try:
            pitch, roll = ilan.hub.imu.tilt()
            if abs(roll) > 50:
                if not roll_exceeded:
                    print(f"Roll exceeded: {roll}")
                    roll_exceeded = True
                    await stop_all()
                return  # יציאה מהלולאה -> הפונקציה מסתיימת
            else:
                roll_exceeded = False
        except Exception as e:
            print("Error in monitor_roll:", e)
        await wait(50)

async def main_loop():
    runs = [
        # --- משימות עיקריות ---
        ("0", "funk",         Icon.TRIANGLE_UP),
        ("1", "funk",         Icon.LEFT),
        ("2", "funk",         Icon.FALSE),
        ("3", "funk",         Icon.HAPPY),
        ("4", "funk",         Icon.SAD),
        ("5", "funk",         Icon.PAUSE),
        ("7", "funk",         Icon.FULL),
        ("8", "funk",         Icon.HEART),

        # --- פעולות נהיגה ---
        (" ", "funk",        Icon.ARROW_LEFT),
        (" ", "funk",        Icon.ARROW_RIGHT),
        (" ", "funk",        Icon.ARROW_LEFT_DOWN),
        (" ", "funk",        Icon.ARROW_LEFT_UP),
        (" ", "funk",        Icon.CLOCKWISE),

        # --- שליטה במנועים ---
        ("1", "funk"),
        ("2", "funk"),
        ("3", "funk"),
        ("4", "funk"),

        # --- בדיקות ופיתוח ---
        ("T", detect_color_and_run),
    ]

    await ilan.battery_status()
    buttery_status_timer = StopWatch()
    while True:
        if buttery_status_timer.time() > 10000:
            await ilan.battery_status()
            buttery_status_timer.reset()
    

async def main():
    while True:
        await multitask(monitor_roll(), detect_color_and_run())


async def color_detection_task():
    while True:
        # await ilan.color_sensor.color()
        color = ilan.color_sensor.color()

            # Print the measured color and reflection.
        # print(await ilan.color_sensor.hsv%())

            # Move the sensor around and see how
            # well you can detect colors.

            # Wait so we can read the value.
        await wait(1000)

    

run_task(main_loop())