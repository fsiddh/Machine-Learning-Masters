import pandas as pd
import en_core_web_sm
from com_in_ineuron_ai_utils.utils import data_preprocessing_predict, preprocess_training_data
import pickle
import numpy as np

class PredictApi:

    def __init__(self, stopWordsFilePath):
        self.nlp = en_core_web_sm.load()
        self.stop_words_path = stopWordsFilePath
        self.noOfClasses = ["Negative", "Positive"]

    def executePreocessing(self, text, jsonFilePath,modelPath,vectorPath):
        df_pred = pd.DataFrame([text],columns=['text'])
        df_pred['text'] = data_preprocessing_predict(df_pred['text'], self.stop_words_path)
        df_pred['text'] = [" ".join(value) for value in df_pred['text'].values]

        with open(vectorPath,'rb') as f:
            vectorizer = pickle.load(f)
        with open(modelPath, 'rb') as f:
            model = pickle.load(f)
        pred_vector_ = vectorizer.transform(df_pred['text'])
        prediction = model.predict(pred_vector_)
        predictedProbability = model.predict_proba(pred_vector_)
        if list(predictedProbability.flatten())[0] == list(predictedProbability.flatten())[1]:
            return "UNKNOWN"
        elif list(predictedProbability.flatten())[np.argmax(predictedProbability)] > .3:
            return prediction
        else:
            return "UNKNOWN"










