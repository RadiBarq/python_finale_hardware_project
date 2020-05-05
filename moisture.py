import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class Moisture:

	def __init__(self):
		# Create the I2C bus
		i2c = busio.I2C(board.SCL, board.SDA)

		# Create the ADC object using the I2C bus		
		self.ads = ADS.ADS1015(i2c)

	def getMoisture(self):
		# Create single-ended input on channel 0
		chan = AnalogIn(self.ads, ADS.P2)
		#print("{:>5}\t{:>5}".format('raw', 'v'))
		voltage = chan.voltage
		moisture_percentage = 100 - voltage/3.85 * 100
		#print("{:>5}\t{:>5.3f}%".format(chan.value, moisture_percentage))
		return moisture_percentage