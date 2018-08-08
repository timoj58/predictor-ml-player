from util.config_utils import get_dir_cfg
import os.path
import os
import requests
import logging

logger = logging.getLogger(__name__)


aws = get_dir_cfg()['aws']
aws_url = get_dir_cfg()['aws_url']

local_dir = get_dir_cfg()['local']


def on_finish(tf_models_dir, aws_model_dir):
    logger.info(' write index '+tf_models_dir)
    write_filenames_index(tf_models_dir)
    write_filenames_index(tf_models_dir+'/eval')
    logger.info(' put aws files '+aws_model_dir)
    put_aws_files_from_dir(aws_model_dir+'/')
    put_aws_files_from_dir(aws_model_dir+'/eval/')
    logger.info(' clearing directory')
    clear_directory(tf_models_dir)


def clear_directory(path):
   if aws:
    for file in os.listdir(path):
      if not os.path.isdir(path+'/'+file):
       if file != "index.txt": #dont delete the index...doh.
        logger.info(' deleting '+file)
        file_path = os.path.join(path, file)
        os.unlink(file_path)


def get_indexes(path):
    if  os.path.isfile(path+'/index.txt'):
     file = open(path+'/index.txt', 'r')
     return file.readlines()
    return []

def is_in_index(path, filename):
    onfile = False
    indexes = get_indexes(path)
    for index in indexes:
       if index.strip('\n') == filename:
           onfile = True
    return onfile

def write_filenames_index_from_filename(filename):
    head, tail = os.path.split(filename)
    write_filenames_index(head)

def write_filenames_index(path):
   logger.info("index for "+path)
   indexes = get_indexes(path)
   files = os.listdir(path)
   with open(path+'/index.txt', 'w') as f:
    for file in files:
      if not os.path.isdir(path+'/'+file):
       if file != "index.txt": #dont log the index...doh.
        if file not in indexes:
         logger.info(file)
         f.write(file)
         f.write('\n')


def get_aws_file(path, filename):
   if aws:
    filename = filename.strip('\n')
    logger.info('getting aws file '+aws_url+filename)
    response = requests.get(aws_url+path+filename, headers={})
    with open(local_dir+path+filename, 'wb') as f:
     f.write(response.content)


def put_aws_files_from_dir(path):
  logger.info('getting indexes for '+local_dir+path)
  indexes = get_indexes(local_dir+path)
  for index in indexes:
      put_aws_file_with_path(path, index.strip('\n'))

def put_aws_file_with_path(aws_path, filename):
    if aws:
        head, tail = os.path.split(filename)
        logger.info('putting file to aws - '+aws_url+aws_path+tail)

        with open(local_dir+aws_path+filename,'rb') as filedata:
          requests.put(aws_url+aws_path+tail, data=filedata, headers={})


def put_aws_file(filename):
    if aws:
     head, tail = os.path.split(filename)
     logger.info('putting file to aws - '+aws_url+tail)
     with open(filename, 'rb') as filedata:
         requests.put(aws_url+tail, data=filedata, headers={})

def is_on_file(filename):
    if aws is False:
        return os.path.isfile(filename)
    else:
        head, tail = os.path.split(filename)
        return is_in_index(head, tail)



