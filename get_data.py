# import requests

# resp = requests.get("http://api.census.gov/data/timeseries/healthins/sahie?get=NIC_PT,NAME,NUI_PT&for=us:*&time=2013&key=e0103f837daffd400e2208bacbf97de2be035383")

# if resp.status_code != 200:
# 	print "Error! Request not successful"

# print resp.json 


import urllib2
import json 

# req = urllib2.Request("http://api.census.gov/data/timeseries/healthins/sahie?get=NIC_PT,NAME,NUI_PT&for=us:*&time=2013&key=e0103f837daffd400e2208bacbf97de2be035383")
# response = urllib2.urlopen(req)
# the_page = response.read()

# print response.json 
# #print the_page


startYear = 2006
endYear = 2013
myData = []

for year in range(startYear, endYear+1):
	url = "http://api.census.gov/data/timeseries/healthins/sahie?get=NIC_PT,NAME,NUI_PT&for=STATE:025&time=" + str(year)
	yearData = json.load(urllib2.urlopen(url))
	myData.append({year: yearData})


output_name = "yearly_data.txt"

with open(output_name, 'w') as outfile:
    json.dump(myData, outfile)