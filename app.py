import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model =pickle.load(open('Water_Q_rf.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dash.html')
def dash():
    return render_template('dash.html')


@app.route('/predict',methods=['POST'])
def predict():
    try:
      in_u = [np.array([x for x in request.form.values()])]
      print(in_u)
      prediction = model.predict(in_u)
      print(prediction)
      output ="Potable !" if prediction[0]==1 else "Not Potable!"
      return render_template('index.html', prediction_text='Your water sample is {}'.format(output))
    except:
        return render_template('index.html', prediction_text="Invalid Input Try Again!")

if __name__ == "__main__":
    app.run(debug=True)