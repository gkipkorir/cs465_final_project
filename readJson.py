import json

from pprint import pprint 


def getJson():
	with open('newData.json') as data_file:
		data = json.load(data_file)
	return data 
