#SC_1/12/2023

import requests, json

#Get request
ip = "10.38.4.15"
host = "http://" + ip + "/api/v2.0.0/"

#headers formatteren
headers = {}
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Basic ZGlzdHJpYnV0b3I6YjBhOGMwNzI4MzM4YjU0ZGRiYjBkODNkNzk4ZWI2OWY3MWY3YjkyOWViYzY2YTgxNzQxMTc1MWI1YjZkZmNlZA=="

get_missions = requests.get(host + "missions", headers = headers)
print(get_missions.text)
