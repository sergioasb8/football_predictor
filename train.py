# Saving the model

# import libraries
import pandas as pd
import xgboost as xgb
from sklearn.feature_extraction import DictVectorizer
import pickle

# set the parameters
xgb_params = {
    'eta': 0.3, 
    'max_depth': 4,
    'min_child_weight': 1,
    
    'objective': 'binary:logistic',
    'nthread': 8,
    
    'seed': 1,
    'verbosity': 1,
}

data_path = './data/enriched_data/premier_league.csv'

output_file = './models/xgboost_model.bin'


# get the data for the model
data_model = pd.read_csv(data_path)
data_model.columns = data_model.columns.str.lower().str.replace(' ', '_')
most_meaningful_features = ['ftg_scored_total','htg_scored_total','points','goal_difference','position','win_rate','mooving_win_rate','mooving_goals_scored']

# set X and y datasets

model_df = data_model[most_meaningful_features + ['win']].copy()
y_df = model_df.win.values
del model_df['win']

# vectorize the data
dv = DictVectorizer(sparse=False)

X_dict = model_df[most_meaningful_features].to_dict(orient='records')
X_df = dv.fit_transform(X_dict)

features = dv.feature_names_
dx = xgb.DMatrix(X_df, label=y_df, feature_names=features)

# train the model
model = xgb.train(xgb_params, dx, num_boost_round=100)

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)