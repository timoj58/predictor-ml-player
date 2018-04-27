import pandas as pd

# need to map homeWin, draw, awayWin
CSV_COLUMN_NAMES = ['home', 'homePlayer1', 'homePlayer2', 'homePlayer3', 'homePlayer4', 'homePlayer5', 'homePlayer6',
                            'homePlayer7', 'homePlayer8', 'homePlayer9', 'homePlayer10', 'homePlayer11',
                            'homeSub1', 'homeSub2', 'homeSub3',
                            'away', 'awayPlayer1', 'awayPlayer2', 'awayPlayer3', 'awayPlayer4', 'awayPlayer5', 'awayPlayer6',
                            'awayPlayer7', 'awayPlayer8', 'awayPlayer9', 'awayPlayer10', 'awayPlayer11',
                            'awaySub1', 'awaySub2', 'awaySub3',
                            'price',
                            'outcome']

OUTCOMES = ['0-0', '1-1', '2-2', '3-3', '4-4', '5-5', '1-0', '2-0', '3-0', '4-0', '5-0', '6-0', '7-0', '8-0',
            '0-1', '0-2', '0-3', '0-4', '0-5', '0-6', '0-7', '0-8',
            '2-1', '1-2', '3-1', '1-3', '4-1', '1-4', '5-1', '1-5', '6-1', '1-6', '7-1', '1-7', '8-1', '1-8',
            '3-2', '2-3', '4-2', '2-4', '5-2', '2-5', '6-2', '2-6', '7-2', '2-7', '8-2', '2-8',
            '4-3', '3-4', '5-3', '3-5', '6-3', '3-6', '7-3', '3-7', '8-3', '3-8',
            '5-4', '4-5', '6-4', '4-6', '7-4', '4-7', '8-4', '4-8',
            '6-5', '5-6', '7-5', '5-7', '8-5', '5-8']

def load_data(train_path, test_path, y_name='outcome'):
    train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=None)
    train_x, train_y = train, train.pop(y_name)

    converted_train_y = []

    for key in train_y:
        converted_train_y.append(OUTCOMES.index(key))

    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=None)
    test_x, test_y = test, test.pop(y_name)

    converted_test_y = []

    for key in train_y:
        converted_test_y.append(OUTCOMES.index(key))


    return (train_x, converted_train_y), (test_x, converted_test_y)

