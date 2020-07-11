import json
import requests
import pymysql.cursors
connection = pymysql.connect(host='internly-db.co952byay6uw.eu-west-2.rds.amazonaws.com',
                             user='admin',
                             password='tlc041!Durham',
                             db='ollie_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
cursor.execute("SELECT * FROM ollie_db.river_levels")
url = 'https://6eg7g0fy8k.execute-api.eu-west-1.amazonaws.com/river-coding-test'
headers = {'Authorization' : ('token','somehash'), 'Accept' : 
'application/json', 'Content-Type' : 'application/json'}
response = requests.get(url, auth=('user', 'pass'))
json_file = response.json()
print(response.text)
"""
#river_levels = json_file['items']
#river_level, time_level = [], []
#Value of the river level river_levels['value']
#Date is at river_levels[dateTime]
#In format 2000-07-11T05:45:00Z
print(len(river_levels))
id = 1
for time in river_levels:
    time_level = [time['dateTime'], time['value']]
    river_level.append(time_level)
    id += 1
    cursor.execute("INSERT INTO ollie_db.river_levels (id, datetime, level) VALUES ($(id), $(time[0]), $(time[1])")
#river level has each element [time, level]

"""


