import numpy as np
import pandas as pd
import pickle
from flask import Flask,request,jsonify
import dataPrep

# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

app = Flask(__name__)

""" Example Route"""

@app.route('/func', methods=['POST'])
def fun():
     return jsonify(username="tedy",
                       email="tedy@investree.id",
                       id="tedy")

@app.route('/procces',methods=['POST'])
def procces():
    data = request.get_json()

    nama = data['name']
    email = data['email']
    location= data['location']
    randomlist = data['randomlist']
    print('nais')

    return jsonify({'result' : 'Success',
                    'name': nama,
                    'email':email,
                    'location':location,
                    'randomlist':randomlist
                    })


""" Machine learning Route """
# Load the model
model = pickle.load(open('model.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json()
    hist_current = data['hist_current']
    hist_xday = data['hist_xday']
    hist_30dpd = data['hist_30dpd']
    hist_60dpd = data['hist_60dpd']
    hist_npl = data['hist_npl']
    percentage = data['percentage']
    all_hist_current = data['all_hist_current']
    all_hist_xday = data['all_hist_xday']
    all_hist_30dpd = data['all_hist_30dpd']
    all_hist_60dpd = data['all_hist_60dpd']
    all_hist_npl = data['all_hist_npl']
    all_hist_percentage = data['all_hist_percentage']

    # Make prediction using model loaded from disk as per the data.
    datatest = [hist_current,hist_xday,hist_30dpd,hist_60dpd,hist_npl,percentage,all_hist_current,
                all_hist_xday,all_hist_30dpd,all_hist_60dpd,all_hist_npl,all_hist_percentage]

    inputdata = []
    for i in range(len(datatest)):
        inputdata.append(datatest[i])

    ha = np.array(inputdata)

    prediction = model.predict([ha])

    prob = model.predict_proba([ha])

    # Take the value of prediction
    if (int(prediction) == 1):
        output = "Good"
        probvalue = float(prob[0][1])
    else:
        output = "Bad"
        probvalue = float(prob[0][1])

    return (jsonify({
        'hist_current' : hist_current,
    'hist_xday' : hist_xday,
    'hist_30dpd' : hist_30dpd,
    'hist_60dpd' : hist_60dpd,
    'hist_npl' : hist_npl,
    'percentage' : percentage,
    'all_hist_current' : all_hist_current,
    'all_hist_xday' : all_hist_xday,
    'all_hist_30dpd' : all_hist_30dpd,
    'all_hist_60dpd' : all_hist_60dpd,
    'all_hist_npl' : all_hist_npl,
    'all_hist_percentage' : all_hist_percentage,
    'probability value': probvalue,
    'prediction' : output
    }))

def main():
    app.run(port=5000, debug=True)