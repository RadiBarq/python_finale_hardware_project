import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from network_model import NetworkModel

class Moisture:

	def __init__(self):
		# Create the I2C bus
		i2c = busio.I2C(board.SCL, board.SDA)

		# Create the ADC object using the I2C bus		
		self.ads = ADS.ADS1015(i2c)
		self.moisture_percentage = 0

	def execute(self, url):
		# Create single-ended input on channel 0
		chan = AnalogIn(self.ads, ADS.P2)
		#print("{:>5}\t{:>5}".format('raw', 'v'))
		voltage = chan.voltage
		self.moisture_percentage = 100 - voltage/3.85 * 100
		#print("{:>5}\t{:>5.3f}%".format(chan.value, moisture_percentage))
		self.sendToServer(url)
	
	def sendToServer(self, url):
		NetworkModel.postSensorValue(url, {'value': self.moisture_percentage})
	
	def getMoisture(self):
		return self.moisture_percentage

