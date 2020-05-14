import requests

class NetworkModel:

	baseURL = "http://192.168.1.148:8001/"
	planterID = 2
	plantersURL = "{0}api/planters/{1}".format(baseURL ,planterID)
	jobsURL = "{0}/jobs".format(plantersURL)
		
	def __init__(self):
		pass

	# Get all jobs
	@staticmethod
	def getAllJobs():
		return requests.get(NetworkModel.jobsURL)

	# Get one job
	@staticmethod
	def getJob(name):
		uri = "{0}/{1}/".format(NetworkModel.jobsURL, name)
		return requests.get(uri)

	@staticmethod
	def postSensorValue(url, data):
		uri = "{0}{1}".format(NetworkModel.baseURL, url)
		print(uri)
		print(requests.post(uri, json=data))

		
		

		
				
		
		