#Let's start with importing necessary libraries
import pickle
import numpy as np
import pandas as pd

class predObj:

    def predict_log(self, dict_pred):
        with open("standardScalar.sav", 'rb') as f:
            scalar = pickle.load(f)

        with open("modelForPrediction.sav", 'rb') as f:
            model = pickle.load(f)
        data_df = pd.DataFrame(dict_pred,index=[1,])
        scaled_data = scalar.transform(data_df)
        predict = model.predict(scaled_data)
        if predict[0] ==1 :
            result = 'Diabetic'
        else:
            result ='Non-Diabetic'

        return result



