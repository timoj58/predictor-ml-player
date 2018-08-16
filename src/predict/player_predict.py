import json
import util.receipt_utils as receipt_utils
import model.player_model as player_model
from util.model_utils import predict

def predict(data, type, country, player, label, label_values,  model_dir, convert, receipt):


    classifier =  player_model.create(
        type=type,
        country=country,
        player=player,
        train=False,
        label=label,
        label_values=label_values,
        model_dir=model_dir,
        train_filename='',
        test_filename='',
        convert=convert,
        previous_vocab_date="14-08-2018")

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


    expected = [0]
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


    response = predict(
        classifier=classifier,
        predict_x=predict_x,
        label_values=label_values)

    receipt_utils.put_receipt(receipt_utils.PREDICT_RECEIPT_URL, receipt,response)
