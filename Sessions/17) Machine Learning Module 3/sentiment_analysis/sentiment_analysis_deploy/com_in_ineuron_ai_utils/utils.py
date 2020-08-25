import json
import os
import shutil
import en_core_web_sm
import re
import string
import pandas


def createDirectoryForUser(userId, projectId):
    path = os.path.join("trainingData/" + userId)
    if not os.path.isdir(path):
        os.mkdir(path)
    path = os.path.join(path, projectId)
    if not os.path.isdir(path):
        os.mkdir(path)


def dataFromTextFile(filePath):
    stop_wordsList = []
    with open(filePath) as f:
        lines = f.read().splitlines()
        for line in lines:
            stop_wordsList.append(line)
    return stop_wordsList

def data_preprocessing_predict(text_list,filepath):
    stop_words = dataFromTextFile(filepath)
    nlp = en_core_web_sm.load()
    pattern = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

    clean_text = []
    for data in text_list:
        clean_data = []
        doc = nlp(data)
        for token in doc:
            clean = re.sub(pattern, '', str(token.lemma_).lower())
            if clean not in string.punctuation:
                if clean not in stop_words:
                    clean_data.append(clean)
        clean_text.append(clean_data)
    return clean_text

def data_preprocessing_train(data_dict,filepath):
    stop_words = dataFromTextFile(filepath)
    nlp = en_core_web_sm.load()
    pattern = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
    df = pandas.DataFrame(columns=['target', 'text'])
    for key in data_dict.keys():
        clean_text = []
        for line in data_dict[key]:
            # clean_data = []
            doc = nlp(line)
            for token in doc:
                clean = re.sub(pattern, '', str(token.lemma_).lower())
                if clean not in string.punctuation:
                    if clean not in stop_words:
                        clean_text.append(clean)
            # clean_text.append(clean_data)
        df = df.append({'target': key, 'text': clean_text}, ignore_index=True)
    return df


def extractDataFromTrainingIntoDictionary(train_data):
    dict_train_data = {}
    # lNameList = []
    for dict in train_data:
        key_value = dict['lName']
        value = dict['lData']
        # lNameList.append(dict['lName'])
        if key_value not in dict_train_data.keys():
            dict_train_data[key_value] = list([value])
        else:
            (dict_train_data[key_value]).append(value)

    return dict_train_data



# def convertdicttoDataframe(train_user_dict):
#      df = pd.DataFrame()
#      df['target'] = train_user_dict['target']
#      df['text'] = train_user_dict['text']
#
#      return df

def deleteExistingTrainingFolder(path):
    try:
        # if os.path.isdir("ids/" + userName):
        if os.path.isdir(path):
            shutil.rmtree(path)
            return path + ".....deleted successfully.\n"
        else:
            print('File does not exists. ')
    except OSError as s:
        print(s)


def preprocess_training_data(jsonFilePath, stop_words):
    with open(jsonFilePath, 'r') as f:
        data_dict = json.load(f)
    #### Data Cleaning
    clean_df = data_preprocessing_train(data_dict,stop_words)
    # converting preprocesed data from list to string to use in tfIdf
    clean_df['text'] = [" ".join(value) for value in clean_df['text'].values]

    return clean_df
