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

async def all_test():
    """
    מפעיל את כל המנועים ימינה במהירות המקסימלית ועוצר אחרי חמש שניות
    בדיקה למנועים
    """
    ilan.motor_front.run(1000)
    ilan.left_motor.run(1000)
    ilan.right_motor.run(1000)
    ilan.motor_back.run(1000)
    await wait(5000)
    await stop_all()

async def unearth():
    """
     יוצא מהבית האדום ועושה את משימות 1 ו-2
    """
    await multitask(
        ilan.drive_straight(-65, 750), 
        ilan.motor_front.run_until_stalled(-200,duty_limit=40), 
        ilan.motor_back.run_time(200,1600)
    )
    await ilan.turn(110,350)
    await ilan.turn(-30,350)
    await ilan.run_front_motor(200,100)
    await ilan.turn(17)
    await ilan.run_front_motor(100,-95)
    await ilan.drive_until_button(500)
    await ilan.run_front_motor(300,170)
    await ilan.drive_straight_with_pid_old(-1,200,kp=00)
    await ilan.turn_without_right_wheel(-130,450)
    # await multitask( ilan.turn_without_right_wheel(-10,150))#, ilan.run_back_motor(500,260))
    await ilan.drive_straight(-10,450)
    await ilan.motor_back.run_until_stalled(400,duty_limit=40)
    await ilan.drive_straight(-5,450,gradual_stop=False)
    await ilan.run_back_motor(200,-150)
    await multitask(ilan.motor_back.run_until_stalled(-250,duty_limit=55), ilan.motor_front.run_time(250,1), ilan.drive_straight(8,300,False,False,False))
    # await ilan.drive_straight(4,700,False,False,False)
    await ilan.turn(60,400)
    await ilan.drive_straight(60,1000,gradual_stop=False, gradtual_start=False) 



async def mamgura():
    """
    יציאה מבית כחול, ביצוע משימה 8, לאסוף את קרונית הרכבת וחזרה לבית כחול
    """
    await ilan.drive_straight(45,700)
    
    # ביצוע משימה 8

    await ilan.run_front_motor_fast(-85, 0.35)
    await ilan.run_front_motor_fast(85, 0.3) 
    await ilan.run_front_motor_fast(-85, 0.35)
    await ilan.run_front_motor_fast(85, 0.3)
    await ilan.run_front_motor_fast(-85, 0.35)
    await ilan.run_front_motor_fast(85, 0.4)
    
    # נוסע לכיוון הקרונית

    await ilan.turn(-32)
    await ilan.drive_straight(40,700)
    await ilan.turn(-40)
    debug=True
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(35,700)
    await ilan.wait_for_button(debug)
    await ilan.turn(70)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-4,500)
    await ilan.wait_for_button(debug)
    
    # אוסף את הקרונית

    await ilan.run_back_motor(500,55)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-5)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-20,500)
    await ilan.wait_for_button(debug)
    await ilan.turn(-18)
    await ilan.wait_for_button(debug)
    
    # חוזר לבית הכחול

    await ilan.drive_straight(-54,700)

  
async def ritsatMaavar():
    debug=False
    await ilan.drive_straight(17, 700) # יציאה מהבית הכחול למשימה 8
    
    await ilan.run_front_motor_fast(100, 0.32) # ביצוע משימה 8
    await ilan.run_front_motor_fast(-100, 0.35) # ביצוע משימה 8
    await ilan.run_front_motor_fast(100, 0.3)
    await ilan.run_front_motor_fast(-100, 0.35)
    await ilan.run_front_motor_fast(100, 0.3)
    await ilan.run_front_motor_fast(-100, 0.35) # ביצוע משימה 8

    await ilan.drive_straight(-12, 500)
    await ilan.wait_for_button(debug)

    await ilan.turn(-51) # הגעה ממשימה 8 למשימה 9
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(35,800)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor_fast (50, 1.1)
    await ilan.wait_for_button(debug)

    await ilan.drive_straight(-20, 500)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(1.5, 200)
    await ilan.run_front_motor_fast (-60, 0.5)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-10, 500)
    await ilan.wait_for_button(debug) # ביצוע משימה 9
    await ilan.run_front_motor_fast(60, 0.7)
    await ilan.drive_straight(2,200)
    await ilan.wait_for_button(debug)
    await multitask(ilan.turn(-225, 250), ilan.motor_front.run_until_stalled(-1000, duty_limit=75))
    await ilan.drive_straight(-45.5, 700)
    await ilan.turn(90, 400)
    await ilan.drive_straight(-14, 1000, gradtual_start=False, gradual_stop=False)
    await ilan.run_back_motor_fast(time_seconds=1)
    await ilan.run_back_motor_fast(-100, 0.3)
    await ilan.drive_straight(10, 1000, gradtual_start=False, gradual_stop=False)
    await ilan.turn(-80, 400)
    # await ilan.drive_straight2(-85, 1000, gradtual_start=False, gradual_stop=False,stop_at_end=False)
    await multitask(ilan.drive_straight2(-85, 1000, gradtual_start=False, gradual_stop=False,stop_at_end=False), ilan.motor_front.run_until_stalled(-500,duty_limit=75))
    await ilan.turn(-45, 700)
    await ilan.drive_until_touch(-500)


async def elephent():
    """יוצא מבית כחול מבצע משימות 6 7 15 חוזר לבית אדום"""

    #נוסע לכיוון המסימות 5, 6 ו-7
    await ilan.drive_straight(39, 1000)
    await ilan.turn(-25)
    await ilan.drive_straight(35, 700)
    await ilan.turn(83)
    await ilan.drive_straight(11, 500)

    #הופך את רצפות המבנה ומוציא את גושי העפרה 
    await ilan.turn(-32)
    await ilan.turn(16)
    await ilan.drive_straight(1, 200)

    #מרים את המשקולות 
    await ilan.run_front_motor_fast(-46,1.3)
    await ilan.run_front_motor_fast(80,0.7)

    #חוזר לבית הכחול 
    await ilan.drive_straight(-19, 1000)
    await ilan.turn(120,200)
    await ilan.drive_straight(62,1000,gradual_stop=False)




async def skeleton():
    """
    נוסע לכיוון מסימה 14
    """
    await ilan.drive_straight(35,700)  
    await ilan.motor_front.run_until_stalled(500, duty_limit=75)

    # מרים את השלד

    await ilan.run_front_motor(300, -80)
    await multitask (ilan.run_front_motor(110, -300), ilan.drive_straight(3,300))  
    await ilan.drive_straight(5,500)
    await ilan.drive_straight(-15,500)
    



async def cave():

    # יוצא מהבית האדום ועושה את משימות 3 ו-4

    await multitask(ilan.drive_straight2(100, 1000), ilan.motor_front.run_until_stalled(-300,duty_limit=75))
    await ilan.drive_until_touch(250)
    await ilan.drive_straight_with_pid_old(-1.5, 150,gradtual_start=False, gradual_stop=False)
    await ilan.turn(89, 150)

    # מרים את החפץ ומעביר את עגלת מכירות 
 
    await multitask(ilan.motor_front.run_time(300, 2100), ilan.motor_back.run_time(1000, 3000))
    await ilan.drive_straight_with_pid_old(8, 75, kp=00)
    await ilan.run_front_motor(120, -90) 
    await ilan.motor_back.run_time(-1000, 1800)
    await ilan.drive_straight(-12, 125)
    await ilan.run_front_motor(110,-40)
    await ilan.turn(90, 250)

    # חזרה לבית האדום 

    await ilan.drive_straight(80, 1000,gradual_stop=False,gradtual_start=False) 

async def ship():
    """
    יוצא מהבית האדום ועושה את משימות 11 ו-12
    """
    await ilan.drive_straight(58, 500)

    # מבצע את משימה 11

    await ilan.run_front_motor(speed=110, angle=140)
    await ilan.run_back_motor_fast(100, 4)

    # מבצע את משימה 12

    await ilan.drive_straight(-11, 900)
    await ilan.run_front_motor(110, -170)
    await ilan.drive_straight(20, 500,gradual_stop=False)
    await ilan.drive_straight(-69, 1000, gradual_stop=False)




async def main():
        """
        פונקציה המבצעת את כל התכניות
        """
        runs = [
            ("0", elephent , Icon.TRIANGLE_UP),
            ("1", ritsatMaavar , Icon.LEFT),
            ("2", unearth, Icon.FALSE), 
            ("3", cave , Icon.HAPPY),
            ("4", ship, Icon.SAD),
            ("5", skeleton, Icon.PAUSE),
            ("7", all_test, Icon.FULL),

        
        ]
        current_run = 0
        # # await ilan.buttery_status()     
        # buttery_status_timer = StopWatch()   
        # while True:
        #     if buttery_status_timer.time()> 10000:
        #         await ilan.buttery_status()
        #         buttery_status_timer.reset()
        try:
            if (Button.LEFT in ilan.hub.buttons.pressed()):
                current_run += 1
                if current_run >= len(runs):
                    current_run = 0
                if len(runs[current_run]) ==2:
                    ilan.hub.display.char(runs[current_run][0])


            elif (Button.RIGHT in ilan.hub.buttons.pressed()):
                current_run -= 1
                if current_run < 0:
                    current_run = len(runs)-1
                if len(runs[current_run]) ==2:
                    ilan.hub.display.char(runs[current_run][0])
                else:
                    ilan.hub.display.icon(runs[current_run][2])

            elif (Button.BLUETOOTH in ilan.hub.buttons.pressed()):
                await runs[current_run][1]()

                current_run += 1
                if current_run >= len(runs):
                    current_run = 0
                if len(runs[current_run]) ==2:
                    ilan.hub.display.char(runs[current_run][0])
                else:
                    ilan.hub.display.icon(runs[current_run][2])
            else:
                await stop_all()
        except Exception as e:
            print(e)
            raise e
        finally:
            await wait(150)


run_task(main())