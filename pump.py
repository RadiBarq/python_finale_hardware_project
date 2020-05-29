
import RPi.GPIO as GPIO
import time

class Pump:

	pin = 25
	runningTime = 5	
	
	def __init__(self):

		GPIO.setwarnings(False)
		GPIO.setup(Pump.pin, GPIO.OUT)

	def start(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(Pump.pin, GPIO.OUT)
		GPIO.output(Pump.pin, GPIO.HIGH)
		time.sleep(Pump.runningTime)
		GPIO.output(Pump.pin, GPIO.LOW)
