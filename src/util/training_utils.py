import util.receipt_utils as receipt_utils
import dataset.match_dataset as match_dataset
import dataset.player_dataset as player_dataset
import util.model_utils as model_utils
import model.match_model as match_model
import model.player_model as player_model
import util.train_history_utils as train_history_utils


from shutil import copyfile
from util.config_utils import get_dir_cfg
from util.file_utils import is_on_file
from util.file_utils import get_aws_file
from util.file_utils import write_filenames_index_from_filename
from util.file_utils import put_aws_file_with_path

import logging

logger = logging.getLogger(__name__)
local_dir = get_dir_cfg()['local']


def get_range_details(range):

    range = range[1:] #remove first delim
    dates = range.split('/')
    start_date = dates[0]
    end_date = dates[1]
    start = start_date.split('-')
    end = end_date.split('-')

    return int(start[0]), int(start[1]), int(start[2]), int(end[0]), int(end[1]), int(end[2])


def get_next_in_range(range, data):

    next = False

    for val in range:

        if next:
            return val

        if val == data:
            next = True

    return data

def train_match(type, country, data_range, filename_prefix, label, model_dir, train_path, receipt, history, previous_vocab_date):

  for data in data_range:

    train_filename = "train-"+filename_prefix+data.replace('/','-')+".csv"
    test_filename = "test-"+filename_prefix+".csv"
    train_file_path = local_dir+train_path+train_filename
    test_file_path = local_dir+train_path+test_filename


    has_data = model_utils.create_csv(
        url=model_utils.EVENT_MODEL_URL + type+"/"+country,
        filename=train_file_path,
        range=data,
        aws_path=train_path)

    has_test_data = model_utils.create_csv(
        url=model_utils.EVENT_MODEL_URL + type+"/"+country,
        filename=test_file_path,
        range=get_next_in_range(data_range,data),
        aws_path=train_path)

    if has_data == True and has_test_data == False:
        copyfile(train_file_path,
                 test_file_path)
        put_aws_file_with_path(train_path,test_filename)
        write_filenames_index_from_filename(test_file_path)


    if has_data:
        ##take a copy of our file if it doesnt exist.
        #if not is_on_file(test_file_path):
        #    copyfile(train_file_path,
        #             test_file_path)
        #    put_aws_file_with_path(train_path,test_filename)
        #    write_filenames_index_from_filename(test_file_path)
        # else:
        #    get_aws_file(train_path,  test_filename)

        match_model.create(
            type=type,
            country=country,
            train=True,
            label=label,
            label_values=match_dataset.OUTCOMES,
            model_dir=model_dir,
            train_filename=train_path+train_filename,
            test_filename=train_path+test_filename,
            outcome=False,
            previous_vocab_date=previous_vocab_date)
    else:
        logger.info ('no data to train')

    #write the history...
    start_day, start_month, start_year, end_day, end_month, end_year = get_range_details(data)
    history = train_history_utils.create_history('Success - Partial', start_day, start_month, start_year, end_day, end_month, end_year, history['vocab_date'])
    train_history_utils.add_history("country-"+filename_prefix+"-train-history.json", country, history)

  if receipt is not None:
    receipt_utils.put_receipt(receipt_utils.TRAIN_RECEIPT_URL, receipt, None)

  history['status'] = "Success - Full"
  train_history_utils.add_history("country_"+filename_prefix+"-train_history.json", country, history)


def train_player(type, country, player, range, filename_prefix, label, model_dir, train_path, history, previous_vocab_date):

    train_filename = "train-"+filename_prefix+range.replace('/','-')+".csv"
    test_filename = "test-"+filename_prefix+".csv"
    train_file_path = local_dir+train_path+train_filename
    test_file_path = local_dir+train_path+test_filename


    #def create_csv(url, filename, range, aws_path):

    has_data = model_utils.create_csv(
        url=model_utils.PLAYER_MODEL_URL + player,
        train_filename=train_file_path,
        range=range,
        aws_path=train_path)

    if has_data:
        ##take a copy of our file if it doesnt exist.
        if not is_on_file(test_file_path):
            copyfile(train_file_path,
                     test_file_path)
            put_aws_file_with_path(train_path, test_filename)
        else:
            get_aws_file(train_path,  test_filename)

        player_model.create(
            type=type,
            country=country,
            player=player,
            train=True,
            label=label,
            label_values=player_dataset.FIRST_LAST_OUTCOMES,
            model_dir=model_dir,
            train_filename=train_path+train_filename,
            test_filename=train_path+test_filename,
            convert=True,
            previous_vocab_date=previous_vocab_date)
    else:
        logger.info ('no data to train')

    history['status'] = "Success - Full"
    train_history_utils.add_history("players-"+filename_prefix+"-train-history.json", country, history)
