import player_predict as player_predict
import dataset.player_dataset as player_dataset


def predict(data, type, country, player):

    return player_predict.predict(data,
                                  type,
                                  country,
                                  player,
                                  'lastGoal',
                                  player_dataset.FIRST_LAST_OUTCOMES,
                                  "player_last_goal",
                                  "player-last-goal-",
                                  True)
