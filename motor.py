import RPi.GPIO as GPIO
import time

class Motor:
	IN_1 = 26
	IN_2 = 13
	IN_3 = 6
	IN_4 = 5

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(Motor.IN_1, GPIO.OUT)
		GPIO.setup(Motor.IN_2, GPIO.OUT)
		GPIO.setup(Motor.IN_3, GPIO.OUT)
		GPIO.setup(Motor.IN_4, GPIO.OUT)
	
	def backward(self, dur):
		GPIO.output(Motor.IN_1, GPIO.HIGH)
		GPIO.output(Motor.IN_2, GPIO.LOW)
		GPIO.output(Motor.IN_3, GPIO.HIGH)
		GPIO.output(Motor.IN_4, GPIO.LOW)
		time.sleep(dur)
		self.stop()

	def forward(self, dur):
		GPIO.output(Motor.IN_1, GPIO.LOW)
		GPIO.output(Motor.IN_2, GPIO.HIGH)
		GPIO.output(Motor.IN_3, GPIO.LOW)
		GPIO.output(Motor.IN_4, GPIO.HIGH)
		time.sleep(dur)
		self.stop()

	def left(self, dur):
		GPIO.output(Motor.IN_1, GPIO.HIGH)
		GPIO.output(Motor.IN_2, GPIO.LOW)
		GPIO.output(Motor.IN_3, GPIO.LOW)
		GPIO.output(Motor.IN_4, GPIO.HIGH)
		time.sleep(dur)
		self.stop()

	def right(self, dur):
		GPIO.output(Motor.IN_1, GPIO.LOW)
		GPIO.output(Motor.IN_2, GPIO.HIGH)
		GPIO.output(Motor.IN_3, GPIO.HIGH)
		GPIO.output(Motor.IN_4, GPIO.LOW)
		time.sleep(dur)
		self.stop()

	def stop(self):
		GPIO.output(Motor.IN_1, GPIO.LOW)
		GPIO.output(Motor.IN_2, GPIO.LOW)
		GPIO.output(Motor.IN_3, GPIO.LOW)
		GPIO.output(Motor.IN_4, GPIO.LOW)		

motor = Motor()
motor.left(7.8)
motor.backward(2)
