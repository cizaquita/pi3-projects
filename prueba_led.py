import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

def blink():
    print "Ejecucion iniciada..."
    i = 0
    while i < 10:
        print i
        GPIO.output(17, True)
        time.sleep(0.2)
	GPIO.output(22, True)
	time.sleep(0.3)
        GPIO.output(23, True)
	time.sleep(0.4)
        GPIO.output(24, True)
        time.sleep(0.5)


        GPIO.output(17, False)
	time.sleep(0.2)
        GPIO.output(22, False)
	time.sleep(0.3)
        GPIO.output(23, False)
	time.sleep(0.4)
        GPIO.output(24, False)
        
        GPIO.output(27, True)
        time.sleep(0.3)
        GPIO.output(27, False)
        #time.sleep(0.5)
        i = i + 1
    print "fin"
    GPIO.cleanup()
    
blink()