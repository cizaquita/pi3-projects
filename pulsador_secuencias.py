import RPi.GPIO as GPIO
import time
primerLed = 27
segundoLed = 17
tercerLed = 22
cuartoLed = 23
quintoLed = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(segundoLed, GPIO.OUT)
GPIO.setup(primerLed, GPIO.OUT)
GPIO.setup(tercerLed, GPIO.OUT)
GPIO.setup(cuartoLed, GPIO.OUT)
GPIO.setup(quintoLed, GPIO.OUT)


def blink():
    try:
        i = 0
        while True:
            if GPIO.input(25):
                print "Se ha activado el pulsador"
                i = i + 1
                
                if i == 6:
                    i = 1
                
                if i == 1:
                    secuencia1()
                elif i == 2:
                    secuencia2()
                elif i == 3:
                    secuencia3()
                elif i == 4:
                    secuencia4()
                else:
                    secuencia5()
            else:
                print "Esperando " + str(i)
                
    finally:
        GPIO.cleanup()
        

def secuencia2():
    print "Secuencia 1 iniciada..."
    
def secuencia1():
    print "Secuencia 1 iniciada..."
    i = 0
    while i < 5:
        print i
        GPIO.output(primerLed, True)
        time.sleep(0.5)
        GPIO.output(segundoLed, True)
        time.sleep(0.5)
	GPIO.output(tercerLed, True)
	time.sleep(0.5)
        GPIO.output(cuartoLed, True)
	time.sleep(0.5)
        GPIO.output(quintoLed, True)
        time.sleep(0.5)

        GPIO.output(primerLed, False)
        time.sleep(0.5)
        GPIO.output(segundoLed, False)
	time.sleep(0.5)
        GPIO.output(tercerLed, False)
	time.sleep(0.5)
        GPIO.output(cuartoLed, False)
	time.sleep(0.5)
        GPIO.output(quintoLed, False)
        i = i + 1
    print "Fin secuencia 1"
def secuencia3():
    print "Secuencia 3 iniciada..."
    i = 0
    while i < 70:
        print i
        GPIO.output(segundoLed, True)
	GPIO.output(tercerLed, True)
        GPIO.output(cuartoLed, True)
        GPIO.output(quintoLed, True)
        GPIO.output(primerLed, True)
	time.sleep(0.1)

        GPIO.output(segundoLed, False)
        GPIO.output(tercerLed, False)
        GPIO.output(cuartoLed, False)
        GPIO.output(quintoLed, False)
        GPIO.output(primerLed, False)
	time.sleep(0.1)
        i = i + 1
    print "Fin secuencia 3"

def secuencia4():
    print "Secuencia 4 iniciada..."
    i = 0
    while i < 10:
        print i
        GPIO.output(primerLed, True)
        time.sleep(0.1)
        GPIO.output(segundoLed, True)
        time.sleep(0.1)
	GPIO.output(tercerLed, True)
	time.sleep(0.1)
        GPIO.output(cuartoLed, True)
	time.sleep(0.1)
        GPIO.output(quintoLed, True)
        time.sleep(0.1)

        GPIO.output(quintoLed, False)
        time.sleep(0.1)
        GPIO.output(cuartoLed, False)
	time.sleep(0.1)
        GPIO.output(tercerLed, False)
	time.sleep(0.1)
        GPIO.output(segundoLed, False)
	time.sleep(0.1)
        GPIO.output(primerLed, False)
        time.sleep(0.1)
        i = i + 1
    print "Fin secuencia 2"

def secuencia5():
    print "Secuencia 5 iniciada..."
    i = 0
    while i < 10:
        print i
        GPIO.output(tercerLed, True)
        time.sleep(0.3)
        GPIO.output(segundoLed, True)
        GPIO.output(cuartoLed, True)
        time.sleep(0.3)
	GPIO.output(quintoLed, True)
	GPIO.output(primerLed, True)
	time.sleep(0.3)

        GPIO.output(quintoLed, False)
	GPIO.output(primerLed, False)
        time.sleep(0.3)
        GPIO.output(segundoLed, False)
        GPIO.output(cuartoLed, False)
        time.sleep(0.3)
	GPIO.output(tercerLed, False)
        time.sleep(0.3)
        i = i + 1
    print "Fin secuencia 2"


blink()