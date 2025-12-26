


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

async def unearth():
    debug=False
    await ilan.drive_straight(-46, 500)
    await ilan.wait_for_button(debug)
    await ilan.turn(65)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(12, 500)
    await ilan.wait_for_button(debug)
    await ilan.turn(-15)#מפיל את פרח השושנה הימני
    await ilan.wait_for_button(debug)
    await ilan.turn(31)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-10, 500)
    await ilan.wait_for_button(debug)
    await ilan.turn(-7)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(11, 500)
    await ilan.wait_for_button(debug)
    await ilan.motor_front.run_until_stalled(400)
    await ilan.drive_straight(-10)
    await ilan.run_back_motor(500,260)
    await ilan.wait_for_button(debug)
    await ilan.turn(-139)
    await ilan.wait_for_button(True  )
    await ilan.drive_straight(-23, 500)
    await ilan.wait_for_button(debug)
    await ilan.run_back_motor(500,81.67  )
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-6)
    await ilan.motor_back.run_until_stalled(400)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-5)
    await ilan.motor_back.run_until_stalled(-400)
    await ilan.drive_straight(-7)
    await ilan.drive_straight(23,500)
    await ilan.turn(67)
    await ilan.drive_straight(60,700) #חזרה לבית0 0הלבן

  
async def ritsatMaavar():
    debug=False
    await ilan.drive_straight(34, 700) # יציאה מהבית הכחול למשימה 8
    
    await ilan.run_front_motor_fast(100, 0.2) # ביצוע משימה 8
    await ilan.run_front_motor_fast(-100, 0.35) # ביצוע משימה 8
    await ilan.run_front_motor_fast(100, 0.3)
    await ilan.run_front_motor_fast(-100, 0.35)
    await ilan.run_front_motor_fast(100, 0.3)
    await ilan.run_front_motor_fast(-100, 0.35) # ביצוע משימה 8

    await ilan.drive_straight(-12, 500)
    await ilan.wait_for_button(debug)

    await ilan.turn(-53) # הגעה ממשימה 8 למשימה 9
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(33,800)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor_fast (50, 0.35)
    await ilan.wait_for_button(debug)

    await ilan.drive_straight(-17, 500)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor_fast (-60, 0.1)
    # await ilan.drive_straight(0.5, 500)
    await ilan.run_front_motor(500, -50)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-10, 500)
    await ilan.wait_for_button(debug) # ביצוע משימה 9
    await ilan.run_front_motor(300,90)
    await ilan.drive_straight(2,200)
    await ilan.wait_for_button(debug)
    await ilan.turn(-40)
    await ilan.run_front_motor_fast(-100, 0.35) # ביצוע משימה 8
    # await ilan.drive_straight(10,500)
    debug=True
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(48,500)
    await ilan.wait_for_button(debug)
    await ilan.turn(90)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor_fast (50, 0.25)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor_fast (-50, 0.25)
    await ilan.wait_for_button(debug)
    await ilan.turn(-100)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(2,250)
    await ilan.wait_for_button(debug)
    await ilan.motor_back.run_until_stalled(400)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(50,700)
    # await ilan.wait_for_button(debug)
    # await ilan.run_front_motor(5000,-800)
    # await ilan.wait_for_button(debug)
    # await ilan.turn(-30)
    # await ilan.wait_for_button(debug)
    # await ilan.drive_until_touch()
    # await ilan.wait_for_button(debug)
    # await ilan.turn(-20)

    # await ilan.wait_for_button(debug)
    # await ilan.drive_straight(16,500) # הגעה ממשימה 9 למשימה 10

    # await ilan.wait_for_button(debug) # ביצוע משימה 10
    # await ilan.turn(80)
    # await ilan.wait_for_button(debug)
    # await ilan.drive_straight(5,200)
    # await ilan.wait_for_button(debug)
    # await ilan.run_front_motor(800,180)
    # await ilan.wait_for_button(debug)
    # await ilan.run_back_motor(-800,180)   

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

async def elephent():
    # "יוצא מבית כחול מבצע משימות 6 7 15 חוזר לבית אדום
    debug=False

    # await ilan.wait_for_button(debug)
    await ilan.drive_straight(39, 1000)
    # await ilan.wait_for_button(debug)
    await ilan.turn(-25)
    # await ilan.wait_for_button(debug)
    await ilan.drive_straight(35, 700)
    await ilan.wait_for_button(debug)
    await ilan.turn(83)
    # await ilan.wait_for_button(debug)
    await ilan.drive_straight(11, 500)
    
    # await ilan.wait_for_button(debug=True)
    await ilan.turn(-32)
    # await ilan.wait_for_button(debug=True)
    await ilan.turn(20)
    # await ilan.wait_for_button(debug=True)
    # await ilan.drive_until_touch(200)
    await ilan.drive_straight(1, 200)
    # await ilan.wait_for_button(debug=True)
    await ilan.run_front_motor(-200, -210)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor(200, 240)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-19, 1000)
    await ilan.wait_for_button(debug)
    await ilan.turn(110,500)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(65,1000,gradual_stop=False)



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

async def skeleton():
    debug=True
    # await ilan.motor_front.run_until_stalled(-500)
    await ilan.drive_straight(35,700)
    await ilan.wait_for_button(debug)
    await ilan.motor_front.run_until_stalled(200)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(1.5,700)
    await ilan.wait_for_button(debug)
    # await ilan.run_front_motor_fast(-100, 0.3)
    # await ilan.wait_for_button(debug)
    # await ilan.drive_straight(1,100,gradual_stop=False,gradtual_start=False)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor_fast(-100, 0.3)


async def cave():
    #יוצא מהבית האדום ועושה את משימות 3 ו-4
    debug=True
    # await ilan.wait_for_button(debug)
    await multitask(ilan.drive_straight2(100, 1000), ilan.run_front_motor(500, -180))
    # await ilan.wait_for_button(debug) 
    # await ilan.run_back_motor(100,100)
    # await ilan.wait_for_button(debug)
    # await ilan.drive_straight2(100, 1000)
    await ilan.wait_for_button(debug)
    # await ilan.drive_until_button(200)
    # await ilan.wait_for_button(debug)
    await ilan.drive_until_touch(250)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-3, 700)
    await ilan.wait_for_button(debug)
    await ilan.turn(86.5, 150)
    await ilan.wait_for_button(debug)
    await multitask(ilan.motor_front.run_time(300, 1600), ilan.motor_back.run_time(-250,1300)) 
    # await ilan.turn(90, 150)
    # await ilan.wait_for_button(debug)
    # await ilan.motor_front.run_time(1000, 10) # הגעה למשימות 3 ו-4
    # await ilan.run_front_motor(500, -90)
    await ilan.wait_for_button(debug)
    await ilan.motor_back.run_time(500, 4500)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(10.5, 75)
    # await ilan.drive_straight(22.5, 75)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor(100, -65) # ביצוע משימות 3 ו-4
    await ilan.motor_back.run_time(-800, 3000)

    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-22, 125)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor(500, 45)
    await ilan.wait_for_button(debug)
    await ilan.turn(-90, 150)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(85, 700) #חזרה לבית האדום

async def ship():
    debug=True
    await ilan.drive_straight(58, 500)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor(400, 180)
    await ilan.run_back_motor(400, 1000)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-11, 500)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor(500, -180)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(20, 500)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-59, 500)


async def detect_color_and_run():
        print("Starting color detection...")
        #await forum()
        detected_color = await ilan.color_sensor.color()
        print(detected_color)
        await wait(100)

        # match detected_color:

        #     case Color.BLUE:
        #         ilan.hub.display.icon(Icon.TRIANGLE_LEFT)
        #         while True:
        #             if Button.BLUETOOTH in ilan.hub.buttons.pressed():
        #                 # כאן תפעיל פונקציה מתאימה
        #                 await elephent()
        #                 break
        #             else: Button.LEFT in ilan.hub.buttons.pressed()
        #                 # כאן תפעיל פונקציה מתאימה
        #             await skeleton()
        #             break
        #     case Color.GRAY:
        #         ilan.hub.display.icon(Icon.SQUARE)
        #         while True:
        #             if Button.BLUETOOTH in ilan.hub.buttons.pressed():
        #                 await forum()
        #                 break
        #     case Color.YELLOW:
        #         ilan.hub.display.icon(Icon.SAD)
        #         while True:
        #             if Button.BLUETOOTH in ilan.hub.buttons.pressed():  
        #                 await ritsatMaavar()
        #                 break
        #     case Color.WHITE:
        #         ilan.hub.display.icon(Icon.PAUSE)
        #         while True:
        #             if Button.BLUETOOTH in ilan.hub.buttons.pressed():
        #                 await unearth()
        #                 break
        #             elif Button.LEFT in ilan.hub.buttons.pressed():
        #                 await skeleton()
        #                 break
        #             else: Button.RIGHT in ilan.hub.buttons.pressed()
        #             await cave()
        #             break
        #     case Color.RED:
        #         ilan.hub.display.icon(Icon.TRIANGLE_LEFT)
        #         while True:
        #             if Button.BLUETOOTH in ilan.hub.buttons.pressed():
        #                 await ship()
        #                 break
        #     case Color.BLACK:
        #         ilan.hub.display.icon(Icon.CIRCLE)
        #         while True:
        #             if Button.BLUETOOTH in ilan.hub.buttons.pressed():
        #                 await forum()
        #                 break

        if detected_color == Color.BLUE:
            ilan.hub.display.icon(Icon.TRIANGLE_LEFT)
            while True:
                if Button.BLUETOOTH in ilan.hub.buttons.pressed():
                    # כאן תפעיל פונקציה מתאימה
                    await elephent()
                    break
        elif detected_color == Color.BLUE:
            ilan.hub.display.icon(Icon.TRIANGLE_LEFT)
            while True:
                if Button.LEFT in ilan.hub.buttons.pressed():
                    # כאן תפעיל פונקציה מתאימה
                    await skeleton()
                    break

        elif detected_color == Color.GRAY:
            ilan.hub.display.icon(Icon.SQUARE)
            while True:
                if Button.BLUETOOTH in ilan.hub.buttons.pressed():
                    await forum()
                    break

        elif detected_color == Color.YELLOW:
            ilan.hub.display.icon(Icon.SAD)
            while True:
                if Button.BLUETOOTH in ilan.hub.buttons.pressed():  
                    await ritsatMaavar()
                    break
        elif detected_color == Color.WHITE:
            ilan.hub.display.icon(Icon.PAUSE)
            while True:
                if Button.BLUETOOTH in ilan.hub.buttons.pressed():
                    await unearth()
                    break
                elif Button.LEFT in ilan.hub.buttons.pressed():
                    await skeleton()
                    break
                elif Button.RIGHT in ilan.hub.buttons.pressed():
                    await cave()
                    break
        elif detected_color == Color.RED:
            ilan.hub.display.icon(Icon.TRIANGLE_LEFT)
            while True:
                if Button.BLUETOOTH in ilan.hub.buttons.pressed():
                    await ship()
                    break
        
        elif detected_color == Color.BLACK:
            ilan.hub.display.icon(Icon.CIRCLE)
            while True:
                if Button.BLUETOOTH in ilan.hub.buttons.pressed():
                    await forum()
                    break
        
async def test():
    ilan.drive_straight(85)

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
    # runs = [
    #     # --- משימות עיקריות ---
    #     ("0", "funk",         Icon.TRIANGLE_UP),
    #     ("1", "funk",         Icon.LEFT),
    #     ("2", "funk",         Icon.FALSE),
    #     ("3", "funk",         Icon.HAPPY),
    #     ("4", "funk",         Icon.SAD),
    #     ("5", "funk",         Icon.PAUSE),
    #     ("7", "funk",         Icon.FULL),
    #     ("8", "funk",         Icon.HEART),

    #     # --- פעולות נהיגה ---
    #     (" ", "funk",        Icon.ARROW_LEFT),
    #     (" ", "funk",        Icon.ARROW_RIGHT),
    #     (" ", "funk",        Icon.ARROW_LEFT_DOWN),
    #     (" ", "funk",        Icon.ARROW_LEFT_UP),
    #     (" ", "funk",        Icon.CLOCKWISE),

    #     # --- שליטה במנועים ---
    #     ("1", "funk"),
    #     ("2", "funk"),
    #     ("3", "funk"),
    #     ("4", "funk"),

    #     # --- בדיקות ופיתוח ---
    #     ("T", detect_color_and_run),
    # ]
    await detect_color_and_run()

    await ilan.battery_status()
    buttery_status_timer = StopWatch()
    while True:
        if buttery_status_timer.time() > 10000:
            await ilan.battery_status()
            buttery_status_timer.reset()
        
# async def main():
#     while True:
#         await multitask(detect_color_and_run())


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