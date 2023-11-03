# Data source:

The raw data can be found in https://www.football-data.co.uk/data.php

For this project the leagues that will be taken into account are:
    * premier league
    * la liga
    * ligue 1
    * bundesliga
    * primeira liga
    * serie a

The files downloaded from football-data had some issues, some data cleaning was done, with the main focus on deleting columns and seasons with many null values. For this reason, you can find the final datasets for each league in the **data/** folder.


# Columns dictionary

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

# Results dictionary

    * 0 : Lost
    * 1 : Win
    * 2 : Draw