
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
	humidity, temprature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
	if humidity is not None and temprature is not None:
		print("Temp={0:0.1f}C Humadity={1:0.1f}%".format(temprature, humidity))
	else:
		print("Sensor failure. Check wiring.")
	time.sleep(3)
