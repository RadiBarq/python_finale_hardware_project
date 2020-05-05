import picamera
import time

class Camera:
	def __init__(self):
    		pass

	def takePicture(self):
		camera = picamera.PiCamera()
		camera.capture('example.jpg')
