import requests
from requests.auth import HTTPDigestAuth
from util.file_utils import write_csv
from util.auth_utils import auth
from util.config_utils import get_analysis_cfg
from util.file_utils import put_aws_file_with_path
from util.file_utils import write_filenames_index_from_filename
import datetime
from datetime import date, timedelta
import logging
from util.config_utils import get_dir_cfg
import os

logger = logging.getLogger(__name__)

docker_host = get_dir_cfg()['docker_host']


PLAYER_MODEL_URL = docker_host+get_analysis_cfg()['player_model_url']
EVENT_MODEL_URL = docker_host+get_analysis_cfg()['team_model_url']

data_ranges = ['/01-08-2009/01-08-2010','/01-08-2010/01-08-2011','/01-08-2011/01-08-2012','/01-08-2012/01-08-2013',
               '/01-08-2013/01-08-2014','/01-08-2014/01-08-2015','/01-08-2015/01-08-2016','/01-08-2016/01-08-2017',
               '/01-08-2017/01-08-2018']

data_ranges_4 = ['/01-08-2009/01-01-2010','/01-01-2010/01-08-2010','/01-08-2010/01-01-2011','/01-01-2011/01-08-2011',
               '/01-08-2011/01-01-2012','/01-01-2012/01-08-2012','/01-08-2012/01-01-2013','/01-01-2013/01-08-2013',
               '/01-08-2013/01-01-2014','/01-01-2014/01-08-2014', '/01-08-2014/01-01-2015', '/01-01-2015/01-08-2015',
                 '/01-08-2015/01-01-2016', '/01-01-2016/01-08-2016', '/01-08-2016/01-01-2017', '/01-01-2017/01-08-2017',
                 '/01-08-2017/01-01-2018', '/01-01-2018/01-08-2018']

real_time_range = ['/'+ datetime.date.today().strftime('%d-%m-%Y')
                    +'/'
                   + (datetime.date.today() + timedelta(1)).strftime('%d-%m-%Y')]

player_historic_range = '/01-08-2009/13-07-2018'

def create_csv(url, filename, range, aws_path):
    logger.info ('getting csv data...')

    data = requests.get(url+range, headers={'application-token': auth()})

    has_data = write_csv(filename, data)

    if has_data:
      logger.info ('created csv')
      head, tail = os.path.split(filename)
      put_aws_file_with_path(aws_path,tail)
      write_filenames_index_from_filename(filename)


    return has_data
