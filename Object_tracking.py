import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Robot, DistanceSensor
from gpiozero import AngularServo
from time import sleep
import control_data

factory = PiGPIOFactory(host='192.168.137.164')
gpiozero.Device.pin_factory = factory
robot = Robot(left=(18, 23), right=(24, 25), pin_factory=factory)
lowerServo = 2
upperServo = 3
keys = []
myCorrection = 0.45
maxPW = (1.5 + myCorrection) / 1000
minPW = (1.0 - myCorrection) / 1000

panServo = AngularServo(2, min_angle=-180, max_angle=180, initial_angle=0, max_pulse_width=maxPW,
                        min_pulse_width=minPW,
                        pin_factory=factory)
tiltServo = AngularServo(3, min_angle=180, max_angle=-180, initial_angle=0, max_pulse_width=maxPW,
                         min_pulse_width=minPW, pin_factory=factory)


def setservoangle(self, servo, angle):
    servo.angle = angle


def objecttracking(x, y):
    if (x > 350):
        print("servo right")

        if control_data.x < 180:
            control_data.x = control_data.x + 10
            setservoangle(panServo, control_data.x)
            print("Pan Servo:{0}".format(control_data.x))
        else:
            print("Pan Servo: maximum angle ranched")
            panServo.detach()

    if (x < 150):
        print("servo left")
        if control_data.x > -180:
            control_data.x = control_data.x - 10
            setservoangle(panServo, control_data.x)
            print("Pan Servo:{0}".format(control_data.x))
        else:
            print("Pan Servo: maximum angle ranched")
            panServo.detach()

    if (y < 140):
        print("servo up")
        if control_data.y < 140:
            control_data.y = control_data.y + 5
            setservoangle(tiltServo, control_data.y)
            print("Title Servo:{0}".format(control_data.y))
        else:
            print("Title Servo: maximum angle ranched")
            tiltServo.detach()

    if (y > 210):
        print("servo down")
        if control_data.y > -140:
            control_data.y = control_data.y - 5
            setservoangle(tiltServo, control_data.y)
            print("Title Servo:{0}".format(control_data.y))
        else:
            print("Title Servo: maximum angle ranched")
            tiltServo.detach()
