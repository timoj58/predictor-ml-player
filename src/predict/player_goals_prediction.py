import player_predict as player_predict
import dataset.player_dataset as player_dataset


def predict(data, type, country, player):

    return player_predict.predict(data,
                                  type,
                                  country,
                                  player,
                                  'goals',
                                  player_dataset.GOALS_OUTCOMES,
                                  "player_goals",
                                  "player-goals-",
                                  False)
