import joblib
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index.html')

@app.route('/form', methods=["POST"])
def brain():
    try:
        # Extracting data from the form
        Nitrogen = float(request.form['Nitrogen'])
        Phosphorus = float(request.form['Phosphorus'])
        Potassium = float(request.form['Potassium'])
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        Ph = float(request.form['ph'])
        Rainfall = float(request.form['Rainfall'])

        values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]

        # Validate the input values
        if 0 < Ph <= 14 and Temperature < 100 and Humidity > 0:
            # Load the model (ensure the model file is in the correct location)
            # Add this before the joblib.load line
            print("Current directory:", os.getcwd())
            print("Files in current directory:", os.listdir())
            model = joblib.load('crop_app.joblib')
            prediction = model.predict([values])
            return render_template('prediction.html', prediction=str(prediction))
        else:
            return "Sorry... Error in entered values in the form. Please check the values and fill it again."
    except Exception as e:
        # For debugging, print the exception
        print(e)
        return "An error occurred while processing your request."

if __name__ == '__main__':
    app.run(debug=True)



