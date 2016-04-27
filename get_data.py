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

myData = json.load(urllib2.urlopen("http://api.census.gov/data/timeseries/healthins/sahie?get=NIC_PT,NAME,NUI_PT&for=county:*&time=2013"))

year = 2013 
output_name = "county_data_" + str(year) + ".txt"

print output_name

with open(output_name, 'w') as outfile:
    json.dump(myData, outfile)