import pandas as pd

# need to map homeWin, draw, awayWin

CSV_COLUMN_NAMES = ['opponent', 'home', 'minutes', 'saves', 'conceded', 'goals', 'assists']

## fix me.  needs to be an array generated of 0 to 90 integers.
NUMERICS = range(0, 100)
# minutes can go much higher...to confirm if needed.

def load_train_data(train_path, y_name, convert):
    train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=None)
    train_x, train_y = train, train.pop(y_name)

    converted_train_y = []

    if convert is not None:
        for key in train_y:
            converted_train_y.append(convert.index(key))
    else:
        converted_train_y = train_y

    return (train_x, converted_train_y)

def load_data(train_path, test_path, y_name, convert):
 train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=None)
 train_x, train_y = train, train.pop(y_name)

 converted_train_y = []

 if convert is not None:
    for key in train_y:
        converted_train_y.append(convert.index(key))
 else:
        converted_train_y = train_y

 test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=None)
 test_x, test_y = test, test.pop(y_name)

 converted_test_y = []

 if convert is not None:
    for key in test_y:
        converted_test_y.append(convert.index(key))
 else:
    converted_test_y = test_y

 return (train_x, converted_train_y), (test_x, converted_test_y)
