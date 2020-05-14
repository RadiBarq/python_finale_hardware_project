from camera import Camera
from ultrasonic import UltraSonic
from moisture import Moisture
from ldr import LDR
from pump import Pump
from network_model import NetworkModel
import time
from dateutil import parser
import datetime
from humidity import Humidity
from temperature import Temperature

class Main:
	MIN_MOISTURE_THRESHOLD_PERCENTAGE = 30  
	MIN_WATER_LEVEL_THRESHOLD_CM = 4

	def __init__(self):
		# Initialization
		self.camera = Camera()
		self.ultraSonic = UltraSonic()
		self.temperature = Temperature()	
		self.moisture = Moisture()
		self.humidity = Humidity()
		self.pump = Pump()	
		self.ldr = LDR()
		self.jobs = []
		self.filteredJobs = []

	def start(self):
		self.getJobs()
		self.filterJobs()
		self.runJobs()
	
	def getJobs(self):	
		self.jobs = NetworkModel.getAllJobs().json()
					
	def filterJobs(self):
		for job in self.jobs:
			current_time = parser.parse(job["current_time"])
			when_to_execute = job["when_to_execute"]
			last_executed = parser.parse(job["last_executed"])
			time = last_executed + datetime.timedelta(minutes=when_to_execute)
			time = time.replace(tzinfo=None)
			current_time = current_time.replace(tzinfo=None)
			print(current_time)
			print(time)
			print(time >= current_time)
			##if (time >= current_time):
			self.filteredJobs.append(job)

	def runJobs(self):
		print(self.filteredJobs)
		for job in self.filteredJobs:
			jobName = job["name"]
			jobURL = job["job_url"]
			print(jobName)
			if (jobName == "WaterLevel"):
				print("water works")
				## Distance
				self.ultraSonic.execute(jobURL)
				self.waterLevel = self.ultraSonic.getDistance()
				print('distance: {} cm '.format(self.waterLevel))
				time.sleep(1)

			if (jobName == "Temperature"):
				## Temp result
				self.temperature.execute(jobURL)
				time.sleep(1)
			if (jobName == "Humidity"):
				self.humidity.execute(jobURL)
				time.sleep(1)

			if (jobName == "Moisture"):
				## Moisture percentage
				self.moisture.execute(jobURL)
				self.moisturePercentage = self.moisture.getMoisture()
				time.sleep(1)

			if (jobName == "Brightness"):
				##LDR 
				ldrPercentage = self.ldr.execute(jobURL)
				time.sleep(1)
			
			if(jobName == "Camera"):
				self.camera.takePicture()

		if (self.moisturePercentage < Main.MIN_MOISTURE_THRESHOLD_PERCENTAGE and 
			self.waterLevel > Main.MIN_WATER_LEVEL_THRESHOLD_CM):
			print("pump works")
			self.pump.start()


# Start of program
main = Main()
main.start()







