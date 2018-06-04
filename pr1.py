import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

#GPIO.output(27, True)
GPIO.output(17, True)