import requests
from requests.auth import HTTPDigestAuth
import json

def auth():
    # sort this into a config etc for now its for testing
    payload = {'username': 'timmytime', 'password': 'testing'}
    headers = {'content-type': 'application/json'}
    response = requests.post("http://ec2-18-209-13-88.compute-1.amazonaws.com:8091/api/prediction/authenticate",data=json.dumps(payload), headers=headers)
    value = response.json()
    return value['applicationToken']
