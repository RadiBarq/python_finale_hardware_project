import datetime
from dateutil import parser

x = parser.parse("2020-05-08T21:17:18.201657Z")

after_15_minutes = x + datetime.timedelta(minutes = 15)

if (x < after_15_minutes):
	print("it works")

print(x)
print(after_15_minutes)	

