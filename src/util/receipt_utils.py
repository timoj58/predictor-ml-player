import requests
from requests.auth import HTTPDigestAuth
import json
from util.auth_utils import auth
from util.config_utils import get_receipt_cfg
from util.config_utils import get_dir_cfg

docker_host = get_dir_cfg()['docker_host']

TRAIN_RECEIPT_URL = docker_host+get_receipt_cfg()['train_receipt_url']
PREDICT_RECEIPT_URL = docker_host+get_receipt_cfg()['predict_receipt_url']

def put_receipt(url, receipt, result):
    if result is not None:
     headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'application-token': auth()}
     requests.put(url+"?id="+receipt, data=json.dumps(result), headers=headers)
    else:
     requests.put(url+"?id="+receipt, data={}, headers={'application-token': auth()})

