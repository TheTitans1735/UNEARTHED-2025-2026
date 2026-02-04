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
    """""
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

    # await ilan.drive_straight(12, 700)

    # מנקה את משקעי האדמה

    # await ilan.turn(-21, 200)
    # await ilan.turn(37,200)
    # await ilan.drive_straight(-11, 500)
    # await ilan.turn(-8)
    
    # # מוציא את המברשת

    # await ilan.drive_straight(11, 500)
    # await ilan.motor_front.run_until_stalled(400)
    # # await ilan.drive_straight(-10)
    # # await ilan.run_back_motor(500,260)
    # await multitask( ilan.run_back_motor(500,260), ilan.drive_straight(-10))
    # await ilan.turn(-139)
    # await ilan.drive_straight(-29, 500)
    # await ilan.run_back_motor(500,100)
    
    # # מסיר את שכבות הקרקע  

    # await ilan.drive_straight(-11,500)
    # await ilan.drive_straight(3)
    # await ilan.motor_back.run_until_stalled(-400)
    # # await ilan.drive_straight(-13)
    # # await ilan.drive_straight(-3)
    
    # # חוזר לבית האדום

    # await ilan.drive_straight(23,700)
    # await ilan.turn(67,250)
    # await ilan.drive_straight(60,1000,gradual_stop=False, gradtual_start=False) 


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
    await wait(50)
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
    # await ilan.drive_straight(0.5, 500)
    # await ilan.run_front_motor(500, -50)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-10, 500)
    await ilan.wait_for_button(debug) # ביצוע משימה 9
    await ilan.run_front_motor_fast(60, 0.7)
    await ilan.drive_straight(2,200)
    await ilan.wait_for_button(debug)
    await multitask(ilan.turn(-225, 250), ilan.motor_front.run_until_stalled(-1000, duty_limit=75))
    await ilan.drive_straight(-46.5, 700)
    await ilan.turn(90, 400)
    await ilan.drive_straight(-16, 1000, gradtual_start=False, gradual_stop=False)
    await ilan.run_back_motor_fast(100, 0.4)
    await ilan.run_back_motor_fast(-100, 0.3)
    await ilan.drive_straight(10, 1000, gradtual_start=False, gradual_stop=False)
    await ilan.turn(-80, 400)
    # await ilan.drive_straight2(-85, 1000, gradtual_start=False, gradual_stop=False,stop_at_end=False)
    await multitask(ilan.drive_straight2(-85, 1000, gradtual_start=False, gradual_stop=False,stop_at_end=False), ilan.motor_front.run_until_stalled(-500,duty_limit=75))
    await ilan.turn(-45, 700)
    # await ilan.drive_straiht(-50, gradual_stop=False, gradtual_start=False)
    await ilan.drive_until_touch(-500)
    # await ilan.run_front_motor_fast(-100, 0.35) # ביצוע משימה 8
    # # await ilan.drive_straight(10,500)
    # await ilan.wait_for_button(debug)
    # await ilan.drive_straight(46,500)
    # await ilan.wait_for_button(debug)
    # await ilan.turn(87)
    # await wait(500)
    # await ilan.wait_for_button(debug)
    # await ilan.drive_until_button(250)
    # await ilan.run_front_motor_fast (70, 0.5)
    # await ilan.wait_for_button(debug)
    # await ilan.run_front_motor_fast (-70, 0.75)
    # await ilan.drive_straight(-2,250)
    # await ilan.wait_for_button(debug)
    # await ilan.turn(-153)
    # await ilan.wait_for_button(debug)
    # await ilan.drive_straight(4.5,250)
    # # await ilan.drive_until_button(250)
    # await ilan.wait_for_button(debug)
    # await ilan.run_back_motor_fast(-70, 1.2)
    # await ilan.wait_for_button(debug)
    # # await ilan.turn(15)
    # await ilan.drive_base.curve(5,95)
    # await ilan.drive_straight(25)
    # await ilan.turn(-55,250)
    # await ilan.drive_until_button(1000) #חזרה לבית הכחול

async def discover():
  await ilan.drive_straight(-40, 500)
  await ilan.turn(74)
  await ilan.drive_straight(75, 500)
  await ilan.turn(8)
  await ilan.turn(-24)
  await ilan.drive_straight(-7, 500)
  await ilan.turn(-9)
  await ilan.drive_straight
  # לא גמור👌

async def elephent():
    # "יוצא מבית כחול מבצע משימות 6 7 15 חוזר לבית אדום

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
    await ilan.run_front_motor_fast(80,0.6)

    #חוזר לבית הכחול 
    await multitask(ilan.drive_straight(-19, 1000),ilan.motor_front.run_until_stalled(150,duty_limit=45))
    await ilan.turn(120,200)
    await ilan.drive_straight(62,1000,gradual_stop=False)



async def forum(): 
    
    await ilan.turn(17, speed=150)
    await ilan.drive_straight(71, 700)
    await ilan.turn(58, speed=150)
    await ilan.drive_straight(20, 700)
    await ilan.turn(90, speed=150)
    await ilan.drive_straight(10, 700)
    await ilan.run_front_motor(110, -20)
    await ilan.turn(-11, speed=150)
    await ilan.run_front_motor(110, -70)

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
    """"
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

detected_color_icons= {
    
    # מגדיר אייקון לכל צבע

    Color.BLUE: Icon.TRIANGLE_LEFT,
    Color.YELLOW: Icon.SAD,
    Color.WHITE: Icon.PAUSE,
    Color.RED: Icon.TRIANGLE_LEFT,
    Color.GRAY: Icon.HAPPY,
    Color.BLACK: Icon.HEART,
}


colors_actions={

    # מבצע פעולות לפי צבע וכפתור 

    Color.BLUE:{
        Button.BLUETOOTH: elephent,
    },
    Color.YELLOW:{
        Button.BLUETOOTH: ritsatMaavar,
        Button.RIGHT: mamgura
    },
    Color.WHITE:{
        Button.BLUETOOTH: unearth,
        Button.LEFT: discover,
        Button.RIGHT: cave
    },
    Color.RED:{
        Button.BLUETOOTH: ship
    },
    Color.GRAY:{
        Button.BLUETOOTH: skeleton,
    },
    Color.BLACK:{
        Button.BLUETOOTH: all_test,
    }
}


async def detect_color_and_run():
    """
    בודק את הצבע הנוכחי ומפעיל את השיטה בהתאם
    """
    print("Starting color detection...")
    await ilan.buttery_status()     

    buttery_status_timer = StopWatch() 
    while True:
        if buttery_status_timer.time()> 10000:
            await ilan.buttery_status()
            buttery_status_timer.reset()
        try:
            detected_color = await ilan.color_sensor.color()
            ilan.hub.display.icon(detected_color_icons.get(detected_color, Icon.FALSE))

            if detected_color in colors_actions:
                actions = colors_actions[detected_color]
                for button, action in actions.items():
                    if button in ilan.hub.buttons.pressed():
                        await multitask(action(), stop_if_dressing_removed(), race=True)
        except Exception as e:
            print(f"Error in detect_color_and_run loop: {e}")
            await wait(100)


            # if  detected_color == Color.BLUE:
            #     # ilan.hub.display.icon(Icon.TRIANGLE_LEFT)
               
            #     if Button.BLUETOOTH in ilan.hub.buttons.pressed():
            #         await multitask(elephent(),stop_if_dressing_removed(),race=True)
                    
                
                    
            #     elif Button.LEFT in ilan.hub.buttons.pressed():
            #         await multitask(skeleton(),stop_if_dressing_removed(),race=True)
                    

            # elif detected_color == Color.YELLOW:
            #     # ilan.hub.display.icon(Icon.SAD)
            
            #     if Button.BLUETOOTH in ilan.hub.buttons.pressed():  
            #         await multitask(ritsatMaavar(),stop_if_dressing_removed(),race=True)
                    
            #     elif Button.RIGHT in ilan.hub.buttons.pressed():
            #         await multitask(mamgura(),stop_if_dressing_removed(),race=True)
                    

            # elif detected_color == Color.WHITE:
            #     # ilan.hub.display.icon(Icon.PAUSE)
            
            #     if Button.BLUETOOTH in ilan.hub.buttons.pressed():
            #         await multitask(unearth(),stop_if_dressing_removed(),race=True)
                    
            #     elif Button.LEFT in ilan.hub.buttons.pressed():
            #         await multitask(discover(),stop_if_dressing_removed(),race=True)
                    
            #     elif Button.RIGHT in ilan.hub.buttons.pressed():
            #         await multitask(cave(),stop_if_dressing_removed(),race=True)
                
                    
            # elif detected_color == Color.RED:   
            #     # ilan.hub.display.icon(Icon.TRIANGLE_LEFT)
            #     if Button.BLUETOOTH in ilan.hub.buttons.pressed():
            #         await multitask(ship(),stop_if_dressing_removed(),race=True)
                    
                        
            #     # while True:
            #     #     if Button.BLUETOOTH in ilan.hub.buttons.pressed():
            #     #         # כאן תפעיל פונקציה מתאימה
                        
            #             # break
         
            # # elif detected_color == Color.NONE:
            #     # ilan.hub.display.icon(Icon.FALSE)


async def stop_if_dressing_removed():
    """
    פונקציה שעוצרת את כל המנועים כשההלבשה מוסרת
    """
    while await ilan.color_sensor.color() != Color.NONE:
        await wait(100)
    for _ in range(3):
        await ilan.hub.speaker.beep()   
        await wait(100)
         
        
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



# Start the program
run_task(detect_color_and_run())