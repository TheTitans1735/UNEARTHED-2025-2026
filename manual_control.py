from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor,ForceSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Stop, Icon, Color, Button, Direction
from pybricks.tools import wait, StopWatch
from pybricks.iodevices import XboxController
DEADZONE = 10 
class Robot:
    def __init__(self):
        self.hub = PrimeHub()
        self.left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.D)
        self.motor_front = Motor(Port.E)
        self.motor_back = Motor(Port.C)
        self.color_sensor = ColorSensor(Port.A)
        self.drive_base = DriveBase(self.left_motor, self.right_motor, 62.4, 120)
        self.force_sensor = ForceSensor(Port.B)
        self.xbox = XboxController()
        self.drive_base.use_gyro(True)

    def run(self):
         # אזור מת מתחת לערך זה
        while True:
            left_trigger, right_trigger = self.xbox.triggers()
            pressed = self.xbox.buttons.pressed()
            x, y = self.xbox.joystick_left()  # X = שמאל/ימין, Y = קדימה/אחורה
            # print(f"Joystick: x={x}, y={y}, Right Trigger={right_trigger}, Buttons={pressed}")
    # אם הג'ויסטיק כמעט במרכז -> עצור

            if self.force_sensor.pressed():
                self.xbox.rumble(70)

            if Button.A in pressed:
                self.motor_back.run(100)
            elif Button.B in pressed:
                self.motor_back.run(-100)
            elif Button.X in pressed:
                self.motor_front.run(100)
            elif Button.Y in pressed:
                self.motor_front.run(-100)
            elif Button.A not in pressed and Button.B not in pressed and Button.X not in pressed and Button.Y not in pressed:
                self.motor_back.stop()
                self.motor_front.stop()
                
            # if 10 < right_trigger <= 30:
            #     self.drive_base.drive(50, 0)  
                
            # elif 30 < right_trigger <= 50:
            #     self.drive_base.drive(100, 0)

            # elif 50 < right_trigger <= 70:
            #     self.drive_base.drive(200, 0)

            # elif right_trigger > 70:
            #     self.drive_base.drive(300, 0)
                
            # elif right_trigger <= 10:
            #     self.drive_base.stop()
                
            # if 10 < left_trigger <= 30:
            #     self.drive_base.drive(-50, 0)  # נסיעה אחורה איטית
    
            # elif 30 < left_trigger <= 50:
            #     self.drive_base.drive(-100, 0)
                
            # elif 50 < left_trigger <= 70:
            #     self.drive_base.drive(-200, 0)  
                
            # elif left_trigger > 70:
            #     self.drive_base.drive(-300, 0)      
            
            # elif left_trigger <= 10:
            #     self.drive_base.stop()
                
            
                
            if abs(x) < DEADZONE and abs(y) < DEADZONE:
                self.drive_base.stop()
            elif Button.LB in pressed:
                speed = int(y * 10)
                turn = 0
                self.drive_base.drive(speed, turn)

            elif Button.RB in pressed:
                speed = 0
                turn = int(x * 10)
                self.drive_base.drive(speed, turn)
            
            else:
                # Normal driving, maybe less sensitive turn
                speed = int(y * 10)
                turn = int(x * 5)
                self.drive_base.drive(speed, turn)

            wait(5)  # להמתין קצת לפני הקריאה הבאה

Robot().run()