from camera import Camera
from ultrasonic import UltraSonic
from temprature import Temprature
from moisture import Moisture
from ldr import LDR
from pump import Pump
from network_model import NetworkModel
import time
from dateutil import parser

class Main:
	def __init__(self):
		# Initialization
		self.camera = Camera()
		self.ultraSonic = UltraSonic()
		self.temprature = Temprature()	
		self.moisture = Moisture()
		self.pump = Pump()	
		self.ldr = LDR()
		self.jobs = []
		self.filteredJobs = []

	def start(self):
		self.pump.start()
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
			if ((last_executed + datetime.timedelta(minutes = when_to_execute)) >= current_time):
				self.filteredJobs.append(job)
			
			

	def runJobs(self):
		for job in self.filteredJobs:
			jobName = job["name"]
			if (jobName == "WaterLavel"):
				## Distance
				distance = self.ultraSonic.getDistance()
				print('distance: {} cm '.format(distance))
				time.sleep(1)

			if (jobName == "Temprature"):
				## Temp result
				tempResult = self.temprature.readTempratureAndHumadity()
				time.sleep(1)

			if (jobName == "Moisture"):
				## Moisture percentage
				moisturePercentage = self.moisture.getMoisture()
				print("moisture is {:>5.3f}%".format(moisturePercentage))
				time.sleep(1)

			if (jobName == "Brightness"):
				##LDR 
				ldrPercentage = self.ldr.readLDR()
				time.sleep(1)
			
			if(jobName == "Camera"):
				self.camera.takePicture()


# Start of program
main = Main()
main.start()







