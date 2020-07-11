import json
import requests

url = 'https://environment.data.gov.uk/flood-monitoring/id/stations/0240120/readings?_sorted&_limit=100'
headers = {'Authorization' : ('token','somehash'), 'Accept' : 
'application/json', 'Content-Type' : 'application/json'}
r = requests.get(url, auth=('user', 'pass'))
print(r.raw)

json_file = r.json(items)




