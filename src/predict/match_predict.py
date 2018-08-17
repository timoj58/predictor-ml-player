import util.receipt_utils as receipt_utils
import model.match_model as match_model
from util.config_utils import get_dir_cfg
import util.model_utils as model_utils
import logging

local_dir = get_dir_cfg()['local']
logger = logging.getLogger(__name__)


def predict(data, type, country, label, label_values,  model_dir, outcome, receipt):

#def create(type, country, train, label, label_values, model_dir, train_filename, test_filename, outcome, previous_vocab_date):

    classifier =  match_model.create(
                   type=type,
                   country=country,
                   train=False,
                   label=label,
                   label_values=label_values,
                   model_dir=model_dir,
                   train_filename='',
                   test_filename='',
                   outcome=outcome,
                   previous_vocab_date="XX-XX-XXXX")

    home = []
    homePlayer1 = []
    homePlayer2 = []
    homePlayer3 = []
    homePlayer4 = []
    homePlayer5 = []
    homePlayer6 = []
    homePlayer7 = []
    homePlayer8 = []
    homePlayer9 = []
    homePlayer10 = []
    homePlayer11 = []
    homeSub1 = []
    homeSub2 = []
    homeSub3 = []
    away = []
    awayPlayer1 = []
    awayPlayer2 = []
    awayPlayer3 = []
    awayPlayer4 = []
    awayPlayer5 = []
    awayPlayer6 = []
    awayPlayer7 = []
    awayPlayer8 = []
    awayPlayer9 = []
    awayPlayer10 = []
    awayPlayer11 = []
    awaySub1 = []
    awaySub2 = []
    awaySub3 = []
    outcomes = []

    # Generate predictions from the model
    home.append(data['home'])
    homePlayer1.append(data['homePlayer1'])
    homePlayer2.append(data['homePlayer2'])
    homePlayer3.append(data['homePlayer3'])
    homePlayer4.append(data['homePlayer4'])
    homePlayer5.append(data['homePlayer5'])
    homePlayer6.append(data['homePlayer6'])
    homePlayer7.append(data['homePlayer7'])
    homePlayer8.append(data['homePlayer8'])
    homePlayer9.append(data['homePlayer9'])
    homePlayer10.append(data['homePlayer10'])
    homePlayer11.append(data['homePlayer11'])
    homeSub1.append(data['homeSub1'])
    homeSub2.append(data['homeSub2'])
    homeSub3.append(data['homeSub3'])

    away.append(data['away'])
    awayPlayer1.append(data['awayPlayer1'])
    awayPlayer2.append(data['awayPlayer2'])
    awayPlayer3.append(data['awayPlayer3'])
    awayPlayer4.append(data['awayPlayer4'])
    awayPlayer5.append(data['awayPlayer5'])
    awayPlayer6.append(data['awayPlayer6'])
    awayPlayer7.append(data['awayPlayer7'])
    awayPlayer8.append(data['awayPlayer8'])
    awayPlayer9.append(data['awayPlayer9'])
    awayPlayer10.append(data['awayPlayer10'])
    awayPlayer11.append(data['awayPlayer11'])
    awaySub1.append(data['awaySub1'])
    awaySub2.append(data['awaySub2'])
    awaySub3.append(data['awaySub3'])

    if outcome:
      outcomes.append(data['outcome'])
    #print(data)


    expected = [0]
    if outcome:
        predict_x = {
            'home': home,
            'homePlayer1': homePlayer1,
            'homePlayer2': homePlayer2,
            'homePlayer3': homePlayer3,
            'homePlayer4': homePlayer4,
            'homePlayer5': homePlayer5,
            'homePlayer6': homePlayer6,
            'homePlayer7': homePlayer7,
            'homePlayer8': homePlayer8,
            'homePlayer9': homePlayer9,
            'homePlayer10': homePlayer10,
            'homePlayer11': homePlayer11,
            'homeSub1': homeSub1,
            'homeSub2': homeSub2,
            'homeSub3': homeSub3,
            'away': away,
            'awayPlayer1': awayPlayer1,
            'awayPlayer2': awayPlayer2,
            'awayPlayer3': awayPlayer3,
            'awayPlayer4': awayPlayer4,
            'awayPlayer5': awayPlayer5,
            'awayPlayer6': awayPlayer6,
            'awayPlayer7': awayPlayer7,
            'awayPlayer8': awayPlayer8,
            'awayPlayer9': awayPlayer9,
            'awayPlayer10': awayPlayer10,
            'awayPlayer11': awayPlayer11,
            'awaySub1': awaySub1,
            'awaySub2': awaySub2,
            'awaySub3': awaySub3,
            'outcome' : outcomes
        }
    else:
     predict_x = {
        'home': home,
        'homePlayer1': homePlayer1,
        'homePlayer2': homePlayer2,
        'homePlayer3': homePlayer3,
        'homePlayer4': homePlayer4,
        'homePlayer5': homePlayer5,
        'homePlayer6': homePlayer6,
        'homePlayer7': homePlayer7,
        'homePlayer8': homePlayer8,
        'homePlayer9': homePlayer9,
        'homePlayer10': homePlayer10,
        'homePlayer11': homePlayer11,
        'homeSub1': homeSub1,
        'homeSub2': homeSub2,
        'homeSub3': homeSub3,
        'away': away,
        'awayPlayer1': awayPlayer1,
        'awayPlayer2': awayPlayer2,
        'awayPlayer3': awayPlayer3,
        'awayPlayer4': awayPlayer4,
        'awayPlayer5': awayPlayer5,
        'awayPlayer6': awayPlayer6,
        'awayPlayer7': awayPlayer7,
        'awayPlayer8': awayPlayer8,
        'awayPlayer9': awayPlayer9,
        'awayPlayer10': awayPlayer10,
        'awayPlayer11': awayPlayer11,
        'awaySub1': awaySub1,
        'awaySub2': awaySub2,
        'awaySub3': awaySub3
    }


    response = model_utils.predict(
        classifier=classifier,
        predict_x=predict_x,
        label_values=label_values)


    match_model.tidy_up(local_dir+'/models/'+model_dir+'/'+type+'/'+country,None, None, None)
    receipt_utils.put_receipt(receipt_utils.PREDICT_RECEIPT_URL, receipt,response)
