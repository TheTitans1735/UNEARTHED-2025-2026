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
    await ilan.drive_straight(-46, 750)
    await ilan.wait_for_button(debug)
    await ilan.turn(65)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(12, 700)
    await ilan.wait_for_button(debug)
    await ilan.turn(-21, 200)#פיל את פרח השושנה הימני
    await ilan.wait_for_button(debug)
    await ilan.turn(37,200)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-11, 500)
    await ilan.wait_for_button(debug)
    await ilan.turn(-8)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(11, 500)
    await ilan.wait_for_button(debug)
    await ilan.motor_front.run_until_stalled(400)
    await ilan.drive_straight(-10)
    await ilan.run_back_motor(500,260)
    await ilan.wait_for_button(debug)
    await ilan.turn(-139)
    await ilan.drive_straight(-29, 500)
    await ilan.wait_for_button(debug)
    await ilan.run_back_motor(500,100)
    await ilan.drive_straight(-11,500)
    await ilan.drive_straight(3)
    await ilan.wait_for_button(debug)
    await ilan.motor_back.run_until_stalled(-400)
    await ilan.drive_straight(-13)
    # await ilan.motor_back.run_until_stalled(-400)
    await ilan.drive_straight(-3)
    await ilan.drive_straight(23,700)
    await ilan.turn(67)
    await ilan.drive_straight(60,1000) #חזרה לבית0 0הלבן


async def mamgura():
    debug=False
    await ilan.drive_straight(45,700)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor_fast(-85, 0.35) # ביצוע משימה 8
    await ilan.run_front_motor_fast(85, 0.3) # ביצוע משימה 8
    await ilan.run_front_motor_fast(-85, 0.35)
    await ilan.run_front_motor_fast(85, 0.3)
    await ilan.run_front_motor_fast(-85, 0.35)
    await ilan.run_front_motor_fast(85, 0.4)
    await ilan.wait_for_button(debug)
    await ilan.turn(-32)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(40,700)
    await ilan.wait_for_button(debug)
    await ilan.turn(-40)
    debug=True
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(35,700)
    await ilan.wait_for_button(debug)
    await ilan.turn(70)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-4,500)
    await ilan.wait_for_button(debug)
    await ilan.run_back_motor(500,55)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-5)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-20,500)
    await ilan.wait_for_button(debug)
    await ilan.turn(-18)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-54,700)

  
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

    await ilan.turn(-51) # הגעה ממשימה 8 למשימה 9
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(35,800)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor_fast (50, 1)
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
    await ilan.turn(-35, 170)
    await ilan.run_front_motor_fast(-100, 0.35) # ביצוע משימה 8
    # await ilan.drive_straight(10,500)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(46,500)
    await ilan.wait_for_button(debug)
    await ilan.turn(87)
    await wait(500)
    await ilan.wait_for_button(debug)
    await ilan.drive_until_button(250)
    await ilan.run_front_motor_fast (50, 0.5)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor_fast (-50, 0.75)
    await ilan.drive_straight(-2,250)
    await ilan.wait_for_button(debug)
    await ilan.turn(-153)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(4.5,250)
    # await ilan.drive_until_button(250)
    await ilan.wait_for_button(debug)
    await ilan.run_back_motor_fast(-70, 1.2)
    await ilan.wait_for_button(debug)
    # await ilan.turn(15)
    await ilan.drive_base.curve(5,95)
    await ilan.drive_straight(25)
    await ilan.turn(-55,250)
    await ilan.drive_straight(111,1000,gradual_stop=False) #חזרה לבית הכחול
    # await ilan.turn(-30)
    # await ilan.drive_straight(45)
    # await ilan.turn(-25,500)
    # await ilan.drive_straight(60,250)
    # await ilan.drive_straight(50,700)
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
    await ilan.turn(16)
    # await ilan.wait_for_button(debug=True)
    # await ilan.drive_until_touch(200)
    await ilan.drive_straight(1, 200)
    # await ilan.wait_for_button(debug=True)
    await ilan.run_front_motor_fast(-46,1.3)
    await ilan.run_front_motor_fast(80,0.8)
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
    debug=False
    # await ilan.motor_front.run_until_stalled(-500)
    await ilan.drive_straight(35,700)
    await ilan.wait_for_button(debug)
    await ilan.motor_front.run_until_stalled(200)
    await ilan.wait_for_button(debug)
    # await ilan.drive_straight(2.45,700)
    # await ilan.wait_for_button(debug)
    await ilan.run_front_motor(300, -80)
    await ilan.wait_for_button(debug)
    # await ilan.run_front_motor_fast(-100, 0.3)
    # await ilan.wait_for_button(debug)
    # await ilan.drive_straight(1,100,gradual_stop=False,gradtual_start=False)
    await multitask (ilan.run_front_motor(950, -300), ilan.drive_straight(3,300))
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(5,500)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-15,500)
    # await ilan.drive_straight(-2.5,750)
    # await ilan.wait_for_button(debug)
    # await ilan.run_front_motor(500, -150)
    # await ilan.wait_for_button(debug)
    # await ilan.run_front_motor(500, -20)
    # await ilan.wait_for_button(debug)
    # await multitask(ilan.drive_straight(5, 100), ilan.run_front_motor(500, -20))



async def cave():
    #יוצא מהבית האדום ועושה את משימות 3 ו-4
    debug=False

    # await ilan.wait_for_button(debug)
    await multitask(ilan.drive_straight2(100, 1000), ilan.motor_front.run_until_stalled(-300))
    # await ilan.wait_for_button(debug) 
    # await ilan.run_back_motor(100,100)
    await ilan.wait_for_button(debug)
    # await ilan.drive_straight2(100, 1000)
    # await ilan.drive_until_button(200)
    # await ilan.wait_for_button(debug)
    await ilan.drive_until_touch(250)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight_with_pid_old(-1.5, 150,gradtual_start=False, gradual_stop=False)
    await ilan.wait_for_button(debug)
    await ilan.turn(89, 150)
    await ilan.wait_for_button(debug)
    await multitask(ilan.motor_front.run_time(300, 1900),    ilan.motor_back.run_time(1000, 3000))
    # await ilan.turn(90, 150)
    # await ilan.wait_for_button(debug)
    # await ilan.motor_front.run_time(1000, 10) # הגעה למשימות 3 ו-4
    # await ilan.run_front_motor(500, -90)
    await ilan.wait_for_button(debug)

    await ilan.wait_for_button(debug)
    await ilan.drive_straight_with_pid_old(8, 75, kp=00)
    # await ilan.drive_straight(22.5, 75)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor(100, -50) # ביצוע משימות 3 ו-4
    await ilan.motor_back.run_time(-1000, 1800)

    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-12, 125)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor(500,-40)
    await ilan.wait_for_button(debug)
    await ilan.turn(90, 150)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(80, 1000,gradual_stop=False) #חזרה לבית האדום

async def ship():
    await ilan.drive_straight(58, 500)
    await ilan.run_front_motor(speed=400, angle=180)
    await ilan.run_back_motor_fast(100, 6)
    await ilan.drive_straight(-11, 900)
    await ilan.run_front_motor(800, -280)
    await ilan.drive_straight(20, 500)
    await ilan.drive_straight(-69, 800)

detected_color_icons= {
    Color.BLUE: Icon.TRIANGLE_LEFT,
    Color.YELLOW: Icon.SAD,
    Color.WHITE: Icon.PAUSE,
    Color.RED: Icon.TRIANGLE_LEFT,
    Color.NONE: Icon.FALSE
}


colors_actions={
    Color.BLUE:{
        Button.BLUETOOTH: elephent,
        Button.LEFT: skeleton
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
}


async def detect_color_and_run():
        print("Starting color detection...")
        while True:
            #await forum()
            detected_color = await ilan.color_sensor.color()
            ilan.hub.display.icon(detected_color_icons.get(detected_color, Icon.FALSE))

            if detected_color in colors_actions:
                actions = colors_actions[detected_color]
                for button, action in actions.items():
                    if button in ilan.hub.buttons.pressed():
                        await multitask(action(), stop_if_dressing_removed(), race=True)


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
    while await ilan.color_sensor.color() != Color.NONE:
        await wait(100)
    for _ in range(3):
        await ilan.hub.speaker.beep()   
        await wait(100)
         

        
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



# Start the program
run_task(detect_color_and_run())