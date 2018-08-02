import pandas as pd


CSV_COLUMN_NAMES = ['home', 'homePlayer1', 'homePlayer2', 'homePlayer3', 'homePlayer4', 'homePlayer5', 'homePlayer6',
                    'homePlayer7', 'homePlayer8', 'homePlayer9', 'homePlayer10', 'homePlayer11',
                    'homeSub1', 'homeSub2', 'homeSub3',
                    'away', 'awayPlayer1', 'awayPlayer2', 'awayPlayer3', 'awayPlayer4', 'awayPlayer5', 'awayPlayer6',
                    'awayPlayer7', 'awayPlayer8', 'awayPlayer9', 'awayPlayer10', 'awayPlayer11',
                    'awaySub1', 'awaySub2', 'awaySub3',
                    'goals',
                    'firstGoal',
                    'lastGoal']

GOALS_OUTCOMES = [0,1,2,3,4,5,6,7,8,9]
FIRST_LAST_OUTCOMES = [True, False]

def load_data(train_path, test_path, y_name, convert):
    train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=None)
    train_x, train_y = train, train.pop(y_name)

    converted_train_y = []

    if convert:
        for key in train_y:
            converted_train_y.append(convert.index(key))
    else:
        converted_train_y = train_y

    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=None)
    test_x, test_y = test, test.pop(y_name)

    converted_test_y = []

    if convert:
        for key in test_y:
            converted_test_y.append(convert.index(key))
    else:
        converted_test_y = test_y

    return (train_x, converted_train_y), (test_x, converted_test_y)