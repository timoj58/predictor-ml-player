import player_predict as player_predict
import src.dataset.player_dataset as player_dataset


def predict(data, type, country, team):

    return player_predict.predict(data,
                                  type,
                                  country,
                                  team,
                                  'goals',
                                  player_dataset.GOALS_OUTCOMES,
                                  "player_goals",
                                  "player-goals-",
                                  None)
