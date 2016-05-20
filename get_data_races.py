import urllib2
import json 


#global variables 
startYear = 2006
endYear = 2013
myData = {}

for year in range(startYear, endYear+1):
	url = "http://api.census.gov/data/timeseries/healthins/sahie?get=NAME,RACE_DESC,RACECAT,PCTUI_PT&for=state:*&time=" + str(year) 
	yearData = json.load(urllib2.urlopen(url))

	states = []
	state_data = {}

	for i in range(1, len(yearData)):
		# obj_size = len(yearData[i])

		# for j in range(obj_size):
		# 	category_name = yearData[0][j]
		# 	category_value = yearData[i][j]
		# 	state_data[category_name] = category_value

		state_name = yearData[i][0]
		race_object = {}
		race_category = yearData[i][2]
		race_object[race_category] = [yearData[i][3], yearData[i][1]]

		if (state_name in state_data): # state already in dictionary 
			print "found in dictionary!!"

			#add new category 

			temp = state_data[state_name]
			temp[race_category] = [yearData[i][3], yearData[i][1]]
			state_data[state_name] = temp  


		else:
			state_data[state_name] = race_object


	str_year = str(year)
	myData[str_year] = state_data


# save the data in a json file 

output_name = "race_new_Data.json" #"race_data.txt"

with open(output_name, 'w') as outfile:
    json.dump(myData, outfile)



