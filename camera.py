import picamera
import time
import io
from network_model import NetworkModel

class Camera:
	def __init__(self):
		self.camera = picamera.PiCamera()
		self.image_name = 'image.jpeg'

	def execute(self, url):
		self.camera.capture(self.image_name)
		self.sendToServer(url)
		
	def sendToServer(self, url):
		NetworkModel.postImage(url, self.image_name)
		
