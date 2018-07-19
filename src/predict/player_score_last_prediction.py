import player_predict as player_predict
import src.dataset.player_dataset as player_dataset


def predict(data, type, country, team):

    return player_predict.predict(data,
                                  type,
                                  country,
                                  team,
                                  'lastGoal',
                                  player_dataset.FIRST_LAST_OUTCOMES,
                                  "player_last_goal",
                                  "player-last-goal-",
                                  False)
