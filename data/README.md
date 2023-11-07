# Data source:

The raw data can be found in https://www.football-data.co.uk/data.php

For this project the only league to take into account will be the __Premier League__, but you can also find data for the following leagues.

    * premier league
    * la liga
    * ligue 1
    * bundesliga
    * primeira liga
    * serie a

The files downloaded from football-data had some issues, some data cleaning was done, with the main focus on deleting columns and seasons with many null values. For this reason, you can find the final datasets for each league in the **data/** folder.


## Columns dictionary

These are the columns dictionary for the data. The enrichment columns are not included here.

    * Div : League Division
    * Date : Match Date (dd/mm/yy)
    * Time : Time of match kick off
    * HomeTeam : Home Team
    * AwayTeam : Away Team
    * FTHG and HG : Full Time Home Team Goals
    * FTAG and AG : Full Time Away Team Goals
    * FTR and Res : Full Time Result (H:Home Win, D:Draw, A:Away Win)
    * HTHG : Half Time Home Team Goals
    * HTAG : Half Time Away Team Goals
    * HTR : Half Time Result (H:Home Win, D:Draw, A:Away Win)
    * season : season
    * Referee : Referee
    * HS : Home Team Shots
    * AS : Away Team Shots
    * HST : Home Team Shots on Target
    * AST : Away Team Shots on Target
    * HF : Home Team Fouls Committed
    * AF : Away Team Fouls Committed
    * HC : Home Team Corners
    * AC : Away Team Corners
    * HY : Home Team Yellow Cards
    * AY : Away Team Yellow Cards
    * HR : Home Team Red Cards
    * AR : Away Team Red Cards


## Enriched columns

    * Home : 1 - Home, 0 - Away
    * FTG_scored_Total : Full Time Goals Scored Total Amount
    * FTG_received_Total : Full Time Goals Received Total Amount
    * HTG_scored_Total : Half Time Goals Scored Total Amount
    * HTG_received_Total : Half Time Goals Received Total Amount
    * shots_Total : Total Shots
    * shots_received_Total : Total Shots Received
    * shots_target_Total : Total Shots on Target
    * shots_target_received_Total : Total Shots on Target Received
    * fouls_commited_Total : Total Fouls Commited
    * fouls_received_Total : Total Fouls Received
    * corners_Total : Total Corners
    * corners_against_Total : Total Against Corners
    * yellow_cards_Total : Total Yellow Cards
    * yellow_cards_opponent_Total : Total Opponent Yellow Cards
    * red_cards_Total : Total Red Cards
    * red_cards_opponent_Total : Total Opponent Red Cards
    * points : Points at the beginning of the match
    * goal_difference : Goal Difference at the beginning of the match
    * position : Position at the beginning of the match
    * Win : 1 - Win, 0 - [Lost - Draw]
    * win_rate : wins / number_of_matches
    * mooving_win_rate : wins_of_the_last_5_macthes / 5
    * mooving_goals_scored : sum(FTG_scored_Total) / 5
    * mooving_goals_received : sum(FTG_received_Total) / 5


## Raw data to predict

Inside the file **predict_data.csv** there is a sample of raw data available to predict a match. The information available for future matches usually is Date, team names, and season. Since the model needs more data related to the teams there is the notebook **prepare_data_for_predictions.ipynb** where you can input that basic information and get all the necessary input data for the model.


## Input Data to predict

Inside the folder **to_predict/** is an example of matches with all the required information to make predictions. Remember that each row represents an input to predict using the model.

    * ftg_scored_total : total amount of goals scored
    * htg_scored_total : total amount of goals scored during the first half
    * points : points at the start of the match
    * goal_difference : goal difference at the start of the match
    * position : position at the start of the match
    * win_rate : wins / number_of_matches
    * mooving_win_rate : wins_of_the_last_5_macthes / 5
    * mooving_goals_scored : sum(FTG_scored_Total) / 5