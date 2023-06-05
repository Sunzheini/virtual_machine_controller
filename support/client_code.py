import requests
import json


url = 'http://192.168.0.115:5000/command'
headers = {'content-type': 'application/json'}
data = {'command': 'my_command'}
response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.json())
