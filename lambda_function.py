import json
import requests

url = 'https://environment.data.gov.uk/flood-monitoring/id/stations/0240120/readings?_sorted&_limit=100'
headers = {'Authorization' : ('token','somehash'), 'Accept' : 
'application/json', 'Content-Type' : 'application/json'}
response = requests.get(url, auth=('user', 'pass'))
json_file = response.json()
river_levels = json_file['items']
river_level, time_level = [], []
data = []
#Value of the river level river_levels['value']
#Date is at river_levels[dateTime]
#In format 2000-07-11T05:45:00Z
print(len(river_levels))
for time in river_levels:
    time_level = [time['dateTime'], time['value']]
    river_level.append(time_level)
#river level has each element [time, level]
        



