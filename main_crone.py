from camera import Camera
from ultrasonic import UltraSonic
from temprature import Temprature
from moisture import Moisture
from ldr import LDR
import time

camera = Camera()
camera.takePicture()
ultraSonic = UltraSonic()
temprature = Temprature()
moisture = Moisture()
ldr = LDR()

## Distance
distance = ultraSonic.getDistance()
print('distance: {} cm '.format(distance))
time.sleep(1)

## Temp result
tempResult = temprature.readTempratureAndHumadity()
time.sleep(1)


## Moisture percentage
moisturePercentage = moisture.getMoisture()
print("moisture is {:>5.3f}%".format(moisturePercentage))
time.sleep(1)

##LDR 
ldrPercentage = ldr.readLDR()
time.sleep(1)

