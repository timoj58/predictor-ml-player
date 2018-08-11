from predict.player_predict import predict as predict_process
import dataset.player_dataset as player_dataset


def predict(data, type, country, player, receipt):

     predict_process(data,
                     type,
                     country,
                     player,
                     'firstGoal',
                     player_dataset.FIRST_LAST_OUTCOMES,
                     "player_first_goal",
                     True,
                     receipt)
