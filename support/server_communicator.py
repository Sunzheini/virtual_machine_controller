import requests
import json


class ServerCommunicator:
    def __init__(self, url):
        self.url = url

    def send_command(self, command):
        headers = {'content-type': 'application/json'}
        data = {'command': command}
        response = requests.post(self.url, data=json.dumps(data), headers=headers)
        return response.json()
