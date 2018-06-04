import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

def blink():
    try:
        while True:
            time.sleep(0.1)
            if GPIO.input(25):
                print "Se ha activado el pulsador"
                secuencia1()
            else:
                print "Esperando"    
                
    finally:
        GPIO.cleanup()
def secuencia1():
    print "Ejecucion iniciada..."
    i = 0
    while i < 5:
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

blink()