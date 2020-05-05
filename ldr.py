
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class LDR:
	def __init__(self):
		# Create the I2C bus
		i2c = busio.I2C(board.SCL, board.SDA)
 
		# Create the ADC object using the I2C bus		
		self.ads = ADS.ADS1015(i2c)
					
	def readLDR(self):
		# Create single-ended input on channel 0
		chan0 = AnalogIn(self.ads, ADS.P0)
		chan1 = AnalogIn(self.ads, ADS.P1)
		#print("{:>5}\t{:>5}".format('raw', 'v'))
		voltage_0 = chan0.voltage
		voltage_1 = chan1.voltage
		light_percentage_1 = 100 - voltage_0/3.85 * 100
		light_percentage_2 = 100 - voltage_1/3.85 * 100
		print("first ldr is {:>5.3f}%".format(light_percentage_1))
		print("first ldr is {:>5.3f}%".format(light_percentage_2))
					
		