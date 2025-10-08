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
    
    
async def detect_color_and_run():
        detected_color = ilan.color_sensor.color()
        await wait(100)

        if detected_color == Color.CYAN:
            ilan.hub.display.icon(Icon.TRIANGLE_LEFT)
            while True:
                if Button.BLUETOOTH in ilan.hub.buttons.pressed():
                    # כאן תפעיל פונקציה מתאימה
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
            ilan.hub.display.icon(Icon.PAUSE)
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


run_task(main())