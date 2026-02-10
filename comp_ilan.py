# ==================== Imports ====================
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, ForceSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Icon, Color, Button, Direction, Stop
from pybricks.tools import wait, StopWatch, run_task, multitask
from robot import Robot, time_it, over_roll

ilan = Robot()


async def stop_all():
    """עצור את כל המנועים - יחצרים קדמי, אחורי וגלגלים"""
    ilan.drive_base.stop()
    ilan.motor_back.stop()
    ilan.motor_front.stop()


async def all_test():
    """בדיקת כל המנועים - הרץ את כל המנועים במהירות מקסימלית למשך 5 שניות"""
    ilan.motor_front.run(1000)
    ilan.left_motor.run(1000)
    ilan.right_motor.run(1000)
    ilan.motor_back.run(1000)
    await wait(5000)
    await stop_all()


# ------------------------------ משימות -----------------------------
async def unearth():
    """משימה 1-2: יציאה מהבית האדום, הפילת פרחים, הגעה למשימה 2 וחשיפת המפה"""
    # יציאה לכיוון משימה 1 - נסיעה קדימה עם הפעלת מנועים קדמי ואחורי בו זמנית
    await multitask(
        ilan.drive_straight(-65, 750), 
        ilan.motor_front.run_until_stalled(-200, duty_limit=40), 
        ilan.motor_back.run_time(200, 1500)
    )
    
    # סיבובים והפעלות מנוע קדמי - הפלת פרחים
    await ilan.turn(90, 350)
    await ilan.turn(-10, 350)
    await ilan.run_front_motor(200, 100)
    await ilan.turn(17)
    await wait(500)
    
    # הרמת הקלשון
    await ilan.run_front_motor(100, -95)
    await ilan.drive_until_button(500)
    await ilan.run_front_motor(300, 170)
    await ilan.drive_straight_with_pid_old(-1, 200, kp=00)
    
    # נסיעה לכיוון משימה 2 - סיבוב על הגלגל השמאלי בלבד
    await ilan.turn_without_right_wheel(-130, 450)
    await ilan.drive_straight(-10, 450)
    
    # חשיפת חלקי המפה - הפעלת מנוע אחורי עד להתנגשות
    await ilan.motor_back.run_until_stalled(400, duty_limit=40)
    await ilan.drive_straight(-5, 450, gradual_stop=False)
    await ilan.run_back_motor(200, -150)
    await multitask(
        ilan.motor_back.run_until_stalled(-250, duty_limit=55), 
        ilan.motor_front.run_time(250, 1), 
        ilan.drive_straight(8, 300, False, False, False)
    )
   
    # חזרה לבית האדום
    await ilan.turn(60, 400)
    await ilan.drive_straight(60, 1000, gradual_stop=False, gradtual_start=False)


async def flag():
    """משימה: הנחת דגל - נסיעה קדימה, הנחה וחזרה"""
    await ilan.drive_straight(42, 700, gradual_stop=False)
    await ilan.drive_straight(-42, 1000, gradual_stop=False, gradtual_start=False)

  
async def ritsatMaavar():
    """משימה 8-9:  הרמת חפצים, ביצוע משימות 8 ו-9"""
    debug = False
    
    # יציאה מהבית הכחול למשימה 8
    await ilan.drive_straight(17, 700)
    
    # ביצוע משימה 8 - תנועות חוזרות של המנוע הקדמי
    for _ in range(3):
        await ilan.run_front_motor_fast(100, 0.32)
        await ilan.run_front_motor_fast(-100, 0.35) 
        await wait(250)
    
    await ilan.drive_straight(-12, 500)
    await ilan.wait_for_button(debug)

    # הגעה ממשימה 8 למשימה 9
    await ilan.turn(-51) 
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(35, 800)
    await ilan.wait_for_button(debug)
    await ilan.run_front_motor_fast(50, 1.1)
    await ilan.wait_for_button(debug)

    await ilan.drive_straight(-20, 500)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(1.5, 200)
    await ilan.run_front_motor_fast(-60, 0.5)
    await ilan.wait_for_button(debug)
    await ilan.drive_straight(-10, 500)
    await ilan.wait_for_button(debug) 
    
    # ביצוע משימה 9 - הפלה וחזרה
    await ilan.run_front_motor_fast(60, 0.7)
    await ilan.drive_straight(2, 200)
    await ilan.wait_for_button(debug)
    await multitask(
        ilan.turn(-225, 250), 
        ilan.motor_front.run_until_stalled(-1000, duty_limit=75)
    )
    await ilan.drive_straight(-46.5, 700)
    await ilan.turn(90, 400)
    await ilan.drive_straight(-16, 1000, gradtual_start=False, gradual_stop=False)
    await ilan.run_back_motor_fast(100, 0.4)
    await ilan.run_back_motor_fast(-100, 0.3)
    await ilan.drive_straight(10, 1000, gradtual_start=False, gradual_stop=False)
    await ilan.turn(-80, 400)
    await multitask(
        ilan.drive_straight2(-85, 1000, gradtual_start=False, gradual_stop=False, stop_at_end=False), 
        ilan.motor_front.run_until_stalled(-500, duty_limit=75)
    )
    await ilan.turn(-45, 700)
    await ilan.drive_until_touch(-500)

async def elephent():
    """משימה 5-7-15: יציאה מהבית הכחול, הפלת פרחים, הרמת משקולות וחזרה"""
    # נסיעה לכיוון המשימות 5, 6 ו-7
    await ilan.drive_straight(39, 1000)
    await ilan.turn(-25)
    await ilan.drive_straight(35, 700)
    await ilan.turn(83)
    await ilan.drive_straight(11, 500)

    # הפיכת רצפות המבנה ויציאת גושי עפרה
    await ilan.turn(-32)
    await ilan.turn(16)
    await ilan.drive_straight(1, 200)

    # הרמת המשקולות
    await ilan.run_front_motor_fast(-46, 1.3)
    await ilan.run_front_motor_fast(80, 0.6)

    # חזרה לבית הכחול
    await multitask(
        ilan.drive_straight(-10, 1000),
        ilan.motor_front.run_until_stalled(150, duty_limit=45)
    )
    await ilan.turn(-70, 200)
    await ilan.drive_straight(-62, 1000, gradual_stop=False)




async def skeleton():
    """משימה 14: נסיעה לעבר משימה השלד, הרמת השלד וחזרה לבית"""
    # נסיעה לכיוון משימה 14
    await ilan.drive_straight(35, 700)  
    await ilan.motor_front.run_until_stalled(500, duty_limit=75)

    # הרמת השלד
    await ilan.run_front_motor(300, -80)
    await multitask(
        ilan.run_front_motor(110, -300), 
        ilan.drive_straight(3, 300)
    )  
    await ilan.drive_straight(5, 500)
    
    # חזרה לבית האדום
    await ilan.drive_straight(-15, 1000, gradual_stop=False, gradtual_start=False, stop_at_end=False)
    await ilan.turn(25, 300)
    await ilan.drive_straight(-30, 1000, gradual_stop=False, gradtual_start=False)
    



async def cave():
    """משימה 3-4: יציאה מהבית האדום, הרמת חפץ, הגעה למעמד מכירות וחזרה"""
    # יציאה מהבית האדום - נסיעה קדימה עם הפעלת המנוע הקדמי
    await multitask(
        ilan.drive_straight2(100, 1000), 
        ilan.motor_front.run_until_stalled(-300, duty_limit=75)
    )
    await ilan.drive_until_touch(250)
    await ilan.drive_straight_with_pid_old(-1.5, 150, gradtual_start=False, gradual_stop=False)
    await ilan.turn(89, 150)

    # הרמת החפץ והעברת עגלת המכירות
    await multitask(
        ilan.motor_front.run_time(300, 2100), 
        ilan.motor_back.run_time(1000, 3000)
    )
    await ilan.drive_straight_with_pid_old(8, 75, kp=00)
    await ilan.run_front_motor(120, -90) 
    await ilan.motor_back.run_time(-1000, 1800)
    await ilan.drive_straight(-12, 125)
    await ilan.run_front_motor(110, -40)
    await ilan.turn(90, 250)

    # חזרה לבית האדום
    await ilan.drive_straight(80, 1000, gradual_stop=False, gradtual_start=False) 

async def ship():
    """משימה 11-12: יציאה מהבית האדום, הרמת מרכיבים וחזרה"""
    # נסיעה לעבר משימות הספינה
    await ilan.drive_straight(58, 500)

    # ביצוע משימה 11 - הרמת חלקים
    await ilan.run_front_motor(speed=110, angle=140)
    await ilan.run_back_motor_fast(100, 4)

    # ביצוע משימה 12 - עבור ופתיחה
    await ilan.drive_straight(-11, 900)
    await ilan.run_front_motor(110, -170)
    await ilan.drive_straight(20, 500, gradual_stop=False)
    await ilan.drive_straight(-69, 1000, gradual_stop=False)


# ==================== Color Detection Mappings ====================

detected_color_icons = {
    Color.BLUE: Icon.TRIANGLE_LEFT,
    Color.YELLOW: Icon.SAD,
    Color.WHITE: Icon.PAUSE,
    Color.RED: Icon.TRIANGLE_LEFT,
    Color.GRAY: Icon.HAPPY,
    Color.BLACK: Icon.HEART,
}

#מיפוי פעולות לביצוע בהתאם לצבע וכפתור שנלחץ
colors_actions = {
    
    Color.BLUE: {
        Button.BLUETOOTH: elephent,
        Button.RIGHT: flag 
    },
    Color.YELLOW: {
        Button.BLUETOOTH: ritsatMaavar,
    },
    Color.WHITE: {
        Button.BLUETOOTH: unearth,
        Button.RIGHT: cave
    },
    Color.RED: {
        Button.BLUETOOTH: ship
    },
    Color.GRAY: {
        Button.BLUETOOTH: skeleton,
    },
    Color.BLACK: {
        Button.BLUETOOTH: all_test,
    }
}


# ==================== Main Control Functions ====================


async def detect_color_and_run():
    """בדיקת צבע ידית החיישן - בחר משימה בהתאם לצבע ולכפתור שנלחץ"""
    print("Starting color detection...")
    await ilan.buttery_status()     

    buttery_status_timer = StopWatch() 
    while True:
        # בדוק סטטוס סוללה כל 10 שניות
        if buttery_status_timer.time() > 10000:
            await ilan.buttery_status()
            buttery_status_timer.reset()
        try:
            # קרא צבע מהחיישן
            detected_color = await ilan.color_sensor.color()
            ilan.hub.display.icon(detected_color_icons.get(detected_color, Icon.FALSE))

            # בדוק אם יש משימה לצבע זה
            if detected_color in colors_actions:
                actions = colors_actions[detected_color]
                # בדוק איזה כפתור נלחץ וביצע את המשימה המתאימה
                for button, action in actions.items():
                    if button in ilan.hub.buttons.pressed():
                        await multitask(action(), stop_if_dressing_removed(), race=True)
        except Exception as e:
            print(f"Error in detect_color_and_run loop: {e}")
            await wait(100)


async def stop_if_dressing_removed():
    """פונקציה שעוצרת את כל המנועים כאשר ההלבשה מוסרת"""
    # בדוק כל 100ms עד שיישנה הצבע לNONE
    while await ilan.color_sensor.color() != Color.NONE:
        await wait(100)
    # הצפצף 3 פעמים כאות התראה
    for _ in range(3):
        await ilan.hub.speaker.beep()   
        await wait(100)
         
        
async def monitor_roll():
    """פונקציה שמנטרת את זווית ההטיה - עוצרת את כל המנועים אם ההטיה גדולה מ-50 מעלות"""
    roll_exceeded = False
    while True:
        try:
            pitch, roll = ilan.hub.imu.tilt()
            if abs(roll) > 50:
                if not roll_exceeded:
                    print(f"Roll exceeded: {roll}")
                    roll_exceeded = True
                    await stop_all()
                return  # יציאה מהלולאה - הפונקציה מסתיימת
            else:
                roll_exceeded = False
        except Exception as e:
            print("Error in monitor_roll:", e)
        await wait(50)



# ==================== Program Startup ====================
# הפעלת התוכנה - התחל בזיהוי צבע
run_task(detect_color_and_run())