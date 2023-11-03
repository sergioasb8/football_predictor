from flask import Flask, request, jsonify
import pickle
import xgboost as xgb

model_file = './xgboost_model.pkl'
dv_file = './dv.pkl'

# read the model
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

# read the dv
with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)


app = Flask('football_result')

@app.route('/football_result', methods=['POST'])
def predict():

    data = request.get_json()
    # make predictions
    X = dv.fit_transform(data)
    features = dv.feature_names_
    dX = xgb.DMatrix(X, feature_names=features)
    y_pred = model.predict(dX)[0]

    result = {
        'win_probability':float(y_pred),
        'win':bool(y_pred >= 0.5)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 9696)
