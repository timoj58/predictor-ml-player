import pandas as pd
import tensorflow as tf

# need to map homeWin, draw, awayWin

CSV_COLUMN_NAMES = ['home', 'homePlayer1', 'homePlayer2', 'homePlayer3', 'homePlayer4', 'homePlayer5', 'homePlayer6',
                    'homePlayer7', 'homePlayer8', 'homePlayer9', 'homePlayer10', 'homePlayer11',
                    'homeSub1', 'homeSub2', 'homeSub3',
                    'away', 'awayPlayer1', 'awayPlayer2', 'awayPlayer3', 'awayPlayer4', 'awayPlayer5', 'awayPlayer6',
                    'awayPlayer7', 'awayPlayer8', 'awayPlayer9', 'awayPlayer10', 'awayPlayer11',
                    'awaySub1', 'awaySub2', 'awaySub3',
                    'homeWin', 'draw', 'awayWin',
                    'outcome']

OUTCOMES = ['homeWin', 'awayWin', 'draw']



def load_data(train_path, test_path, y_name='outcome'):
    train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=None)
    train_x, train_y = train, train.pop(y_name)

    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=None)
    test_x, test_y = test, test.pop(y_name)

    return (train_x, train_y), (test_x, test_y)


def _parse_line(line):
    # Decode the line into its fields
    fields = tf.decode_csv(line)

    # Pack the result into a dictionary
    features = dict(zip(CSV_COLUMN_NAMES, fields))

    # Separate the label from the features
    label = features.pop('outcome')

    return features, label


def csv_input_fn(csv_path, column_names, batch_size):
    # Create a dataset containing the text lines.
    dataset = tf.data.TextLineDataset(csv_path)

    # Parse each line.
    dataset = dataset.map(_parse_line)

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    return dataset
