# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            number_of_times_pregnant=float(request.json['number_of_times_pregnant'])
            plasma_glucose_concentration = float(request.json['plasma_glucose_concentration'])
            diastolic_blood_pressure = float(request.json['diastolic_blood_pressure'])
            triceps_skinfold_thickness  = float(request.json['triceps_skinfold_thickness'])
            serum_insulin  = float(request.json['serum_insulin'])
            body_mass_index  = float(request.json['body_mass_index'])
            diabetes_pedigree_function = float(request.json['diabetes_pedigree_function'])
            age = float(request.json['age'])

            # Loading the saved models into memory
            filename_scaler = 'scaler_model.pickle'
            filename = 'xgboost_model.pickle'
            scaler_model = pickle.load(open(filename_scaler, 'rb'))
            loaded_model = pickle.load(open(filename, 'rb'))

            # predictions using the loaded model file
            scaled_data=scaler_model.transform([[number_of_times_pregnant,plasma_glucose_concentration,diastolic_blood_pressure,triceps_skinfold_thickness,serum_insulin,body_mass_index,diabetes_pedigree_function, age]])
            prediction=loaded_model.predict(scaled_data)
            print('prediction is', prediction[0])
            if prediction[0]==1:
                result= 'The Patient is Diabetic'
            else:
                result = 'The Patient is not Diabetic'
            # showing the prediction results in a UI
            return jsonify(result)
        except Exception as e:
            print('The Exception message is: ',e)
            return jsonify('error: Something is wrong')
    # return render_template('results.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
   app.run(debug=True) # running the app
