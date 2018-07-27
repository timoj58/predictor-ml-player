import requests
from requests.auth import HTTPDigestAuth
import json
import config_utils as config_utils

def auth():
    auth_details = config_utils.get_auth_cfg()
    # sort this into a config etc for now its for testing
    payload = {'username': auth_details['username'], 'password': auth_details['password']}
    headers = {'content-type': 'application/json'}
    response = requests.post(auth_details['url'],data=json.dumps(payload), headers=headers)
    value = response.json()
    return value['applicationToken']
