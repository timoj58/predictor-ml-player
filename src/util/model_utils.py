import requests
from requests.auth import HTTPDigestAuth
import csv
from util.auth_utils import auth
from util.config_utils import get_analysis_cfg
from util.config_utils import get_dir_cfg
from util.file_utils import put_aws_file
from util.file_utils import write_filenames_index_from_filename


PLAYER_MODEL_URL = get_analysis_cfg()['player_model_url']
EVENT_MODEL_URL = get_analysis_cfg()['team_model_url']


MODEL_RES_DIR = get_dir_cfg()['models']
MODELS_DIR =MODEL_RES_DIR+"models/"

data_ranges = ['/02-08-2009/01-08-2010','/02-08-2010/01-08-2011','/02-08-2011/01-08-2012','/02-08-2012/01-08-2013',
               '/02-08-2013/01-08-2014','/02-08-2014/01-08-2015','/02-08-2015/01-08-2016','/02-08-2016/01-08-2017',
               '/02-08-2017/01-08-2018']

data_ranges_4 = ['/02-08-2009/01-01-2010','/02-01-2010/01-08-2010','/02-08-2010/01-01-2011','/02-01-2011/01-08-2011',
               '/02-08-2011/01-01-2012','/02-01-2012/01-08-2012','/02-08-2012/01-01-2013','/02-01-2013/01-08-2013',
               '/02-08-2013/01-01-2014','/02-01-2014/01-08-2014', '/02-08-2014/01-01-2015', '/02-01-2015/01-08-2015',
                 '/02-08-2015/01-01-2016', '/02-01-2016/01-08-2016', '/02-08-2016/01-01-2017', '/02-01-2017/01-08-2017',
                 '/02-08-2017/01-01-2018', '/02-01-2018/01-08-2018']


def create_csv(url, filename, range):
    print ('getting csv data...')

    data = requests.get(url+range, headers={'application-token': auth()})

    with open(filename, 'w') as f:
     writer = csv.writer(f)
     reader = csv.reader(data.text.splitlines())

     for row in reader:
      writer.writerow(row)

    put_aws_file('',filename)
    write_filenames_index_from_filename(filename)

    print ('created csv')
