import pandas as pd


CSV_COLUMN_NAMES = ['player','home', 'homePlayer1', 'homePlayer2', 'homePlayer3', 'homePlayer4', 'homePlayer5', 'homePlayer6',
                    'homePlayer7', 'homePlayer8', 'homePlayer9', 'homePlayer10', 'homePlayer11',
                    'homeSub1', 'homeSub2', 'homeSub3',
                    'away', 'awayPlayer1', 'awayPlayer2', 'awayPlayer3', 'awayPlayer4', 'awayPlayer5', 'awayPlayer6',
                    'awayPlayer7', 'awayPlayer8', 'awayPlayer9', 'awayPlayer10', 'awayPlayer11',
                    'awaySub1', 'awaySub2', 'awaySub3',
                    'price',
                    'outcome']

OUTCOMES = [0,1,2,3,4,5,6]


def load_data(train_path, test_path, y_name='outcome'):
    train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=None)
    train_x, train_y = train, train.pop(y_name)

    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=None)
    test_x, test_y = test, test.pop(y_name)

    return (train_x, train_y), (test_x, test_y)
