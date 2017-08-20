import RPi.GPIO as gpio
import time

sensing = True
TRIGGER1 = 11
ECHO1 = 13
TRIGGER2 = 21
ECHO2 = 23
PWM_PIN = 12
FORWARD = 16
REVERSE = 18
LEFT = 22
RIGHT = 24
front_sensor = 0
rear_sensor = 0
pins = [7,8,10,11,13,16,18,19]
PWM_LEVEL = 100



def setFalse(mylist):
        for pin_num in mylist:
                gpio.output(pin_num,False)

def setTrue(mylist):
        for pin_num in mylist:
                print(type(pin_num))
                print(pin_num)
                gpio.output(pin_num,True)

def setup():
       
        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False)
        gpio.setup(TRIGGER1, gpio.OUT)
        gpio.setup(ECHO1, gpio.IN)
        gpio.setup(TRIGGER2, gpio.OUT)
        gpio.setup(ECHO2, gpio.IN)
        gpio.setup(PWM_PIN, gpio.OUT)
        pwm = gpio.PWM(PWM_PIN,PWM_LEVEL)
        
        #for pin in pins:
        gpio.setup(pins,gpio.OUT)
                

def move(direction):
        stop()
        print(type(direction))
        setTrue(direction)

def stop():
        setFalse(pins)
        
def cleanup():
	#pwm.stop()
	sensing = False
	gpio.cleanup()
def distance(trigger,echo):
	gpio.output(trigger,False)
	time.sleep(2)
	gpio.output(trigger,True)
	time.sleep(0.00001)
	gpio.output(trigger, False)
	
	while(gpio.input(echo)==0):
		pulse_start = time.time()

	while(gpio.input(echo)==1):
		pulse_end = time.time()

	duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(diatnce,2)
	
	return distance
def getFrontSensorDistance():
	return front_sensor

def getRearSensorDistance():
	return rear_sensor

#while(sensing):
#	front_sensor = distance(TRIGGER1,ECHO1)
#	rear_sensor = distance(TRIGGER2,ECHO2)
