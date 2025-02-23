from gpiozero import Button, LED
from time import sleep
import board
import digitalio
import os
import RPi.GPIO as GPIO
from gpiozero import AngularServo
from RpiMotorLib import rpiservolib 

GPIO_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# GPIO.output(17,GPIO.HIGH)

# Create digital input with pull-up resistor on pin D5
# for break beam sensor.
break_beam = digitalio.DigitalInOut(board.17)
break_beam.direction = digitalio.Direction.INPUT
break_beam.pull = digitalio.Pull.UP

myservotest = rpiservolib.SG90servo("servoone", 50, 3, 11)
# degree = float(input("What degree do you want?\t"))
# print("Duty cycle percent = {} ".format(myservotest.convert_from_degree(degree)))

# 11
# myservotest.servo_sweep(18, 19, 12,4 , 0.5, True, 0.01, 1)

start = 5
wait = 0.001 # seconds
rest = 3

# Main loop runs forever and prints a message once a second
# while the sensor is blocked/broken.
sleep(start)  # Delay for 5 second and repeat again.
while True:
    # Break beam input is at a low logic level, i.e. broken!
    if GPIO.input(GPIO_PIN) != GPIO.HIGH:
        # 2274 x 1516
        os.system('fswebcam -r 2274x1516 --jpeg 100 disposal.jpeg')
        scp ~/extra/civichacks/recycle.py geralyn_chong@10.193.132.92:~/
        if output != trash:
            myservotest.servo_move_step(18, -10, 10, .1, 1, 1, True) # left
        else:
            myservotest.servo_move_step(18, 10, 20, .1, 1, 1, True) # right
        myservotest.servo_move_step(18, 20, 10, .1, 1, 1, True) #neutral
        sleep(10 * rest)
        myservotest  = rpiservolib.SG90servo("servoone", 50, 3, 11)
    sleep(rest)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
# Code for testing the IR sensor
# while True:
#     if GPIO.input(GPIO_PIN) == GPIO.HIGH:
#         print("unblocked")
#     else:
#         print("blocked")
#     sleep(5)
