import RPi.GPIO as GPIO
import time
from network_model import NetworkModel


class UltraSonic:

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		self.TRIG = 18
		self.ECHO = 24
		self.start = 0
		self.end = 0
		self.distance = 0

	def execute(self, url):
		GPIO.setup(self.TRIG, GPIO.OUT)
		GPIO.setup(self.ECHO, GPIO.IN)
		GPIO.output(self.TRIG, True)
		time.sleep(0.0001)
		GPIO.output(self.TRIG, False)
		while GPIO.input(self.ECHO) == False:
			self.start = time.time()
		while GPIO.input(self.ECHO) == True:
			self.end = time.time()
		sig_time = self.end - self.start
		#cm
		self.distance = sig_time / 0.000058
		self.sendToServer(url)
		GPIO.cleanup()
	
	def getDistance(self):
		return self.distance

	def sendToServer(self, url):
		NetworkModel.postSensorValue(url, {'value': self.distance})
		
		
		



