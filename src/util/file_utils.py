from util.config_utils import get_dir_cfg
import os.path
import os
import requests

aws = get_dir_cfg()['aws']
aws_url = get_dir_cfg()['aws_url']
models = get_dir_cfg()['models']

local_dir = get_dir_cfg()['local']


def on_finish(tf_models_dir, aws_model_dir):
    write_filenames_index(tf_models_dir)
    write_filenames_index(tf_models_dir+'/eval')
    put_aws_files_from_dir(aws_model_dir)
    put_aws_files_from_dir(aws_model_dir+'/eval')
    clear_directory(tf_models_dir)


def clear_directory(path):
   if aws:
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        os.unlink(file_path)


def get_indexes(path):
    file = open(path+'index.txt', 'r')
    return file.readlines()


def is_in_index(path, filename):
    onfile = False
    indexes = get_indexes(path)
    for index in indexes:
       if index == filename:
           onfile = True
    return onfile

def write_filenames_index_from_filename(filename):
    head, tail = os.path.split(filename)
    write_filenames_index(head)

def write_filenames_index(path):
   indexes = get_indexes(path)
   files = os.listdir(path)
   with open(path+'index.txt', 'w') as f:
    for file in files:
       if file not in indexes:
         print(file)
         f.write(file)
         f.write('\n')


def get_aws_file(path, filename):
   if aws:
    response = requests.get(aws_url+filename, headers={})
    with open(local_dir+path+filename, 'w') as f:
     f.write(response.content)


def put_aws_files_from_dir(path):
  indexes = get_indexes(local_dir+path)
  for index in indexes:
      put_aws_file(path, index)

def put_aws_file(aws_path, filename):
    if aws:
     head, tail = os.path.split(filename)
     requests.put(aws_url+aws_path+tail, data='', headers={}, files={filename})

def is_on_file(filename):
    if aws is False:
        return os.path.isfile(filename)
    else:
        head, tail = os.path.split(filename)
        return is_in_index(head, tail)



