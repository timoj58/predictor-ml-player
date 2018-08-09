from predict.player_predict import predict as predict_process
import dataset.player_dataset as player_dataset


def predict(data, type, country, player, receipt):

    return predict_process(data,
                                  type,
                                  country,
                                  player,
                                  'lastGoal',
                                  player_dataset.FIRST_LAST_OUTCOMES,
                                  "player_last_goal",
                                  "player-last-goal-",
                                  True)
