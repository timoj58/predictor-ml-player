from predict.player_predict import predict as predict_process
import dataset.player_dataset as player_dataset


def predict(data, type, country, player, receipt):

     predict_process(
         data=data,
         type=type,
         country=country,
         player=player,
         label='firstGoal',
         label_values=player_dataset.FIRST_LAST_OUTCOMES,
         mode_dir="player_first_goal",
         convert=True,
         receipt=receipt)
