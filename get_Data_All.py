import urllib2
import json 

# req = urllib2.Request("http://api.census.gov/data/timeseries/healthins/sahie?get=NIC_PT,NAME,NUI_PT&for=us:*&time=2013&key=e0103f837daffd400e2208bacbf97de2be035383")
# response = urllib2.urlopen(req)
# the_page = response.read()

# print response.json 
# #print the_page

startYear = 2006
endYear = 2013
myData = {}

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'District of Columbia':'DC',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

for year in range(startYear, endYear+1):
	# url = "http://api.census.gov/data/timeseries/healthins/sahie?get=NIC_PT,NAME,NUI_PT&for=STATE:010&time=" + str(year)
	# url = "http://api.census.gov/data/timeseries/healthins/sahie?get=NIC_PT,NAME,NUI_PT&for=us:*&time=2013"
	#url = "http://api.census.gov/data/timeseries/healthins/sahie?get=IPR_DESC,IPRCAT,PCTIC_PT,NAME&for=state:024,025&time=" + str(year)
	url = "http://api.census.gov/data/timeseries/healthins/sahie?get=NAME,NIC_PT,NUI_PT&for=state:*&time=" + str(year)
	yearData = json.load(urllib2.urlopen(url))

	print "yearData", yearData[1][1]

	states = []
	for i in range(1, len(yearData)):
		state_info = {}
		for j in range(len(yearData[0])):
			state_info[yearData[0][j]] = yearData[i][j]
            # state_info.append([])
		
		#Add state abbreviation 
		state_abrev = us_state_abbrev[state_info["NAME"]] 
		state_info["abrev"] = state_abrev
		#print state_abrev

		#add perent unInusred 
		numInsured = int(state_info["NIC_PT"])
		numUnInsured = int(state_info["NUI_PT"])
		percUnInsured = str((numUnInsured*1.0/(numInsured+numUnInsured)) * 100)

		#print percUnInsured

		state_info["PUI"] = percUnInsured

		states.append(state_info)


	str_year = str(year)
	#loop through all the data 
	# for year in yearData:
	# 	print ()
	#myData.append({year: yearData})

	newYearData = {"year": year, "states": states}
	myData[str_year] = newYearData


# for year in range(startYear, endYear+1):
# 	str_year = str(year)
# 	yearData = myData[str_year]

	#print myData[str_year][1]



output_name = "all_Data.json" #"race_data.txt"

with open(output_name, 'w') as outfile:
    json.dump(myData, outfile)
