
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17


class Temprature:
	def __init__(self):
		pass

	def readTempratureAndHumadity(self):
		humidity, temprature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
		if humidity is not None and temprature is not None:
			print("Temp={0:0.1f}C Humadity={1:0.1f}%".format(humidity, temprature))
		else:
			print("cannot read the humidity and temprature")