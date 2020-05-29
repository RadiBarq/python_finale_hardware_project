	

import Adafruit_DHT
import time
from network_model import NetworkModel

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17

class Humidity:
	def __init__(self):
		self.temperature = 0
		self.humidity = 0
		pass

	def execute(self, url):
		self.humidity, self.temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
		if self.humidity is not None and self.temperature is not None:
			print("Temp={0:0.1f}C Humadity={1:0.1f}%".format(self.humidity, self.temperature))
		else:
			print("cannot read the humidity and temprature")

		self.sendToServer(url)

	def sendToServer(self, url):
		print(self.humidity)
		NetworkModel.postSensorValue(url, {'value': self.humidity})