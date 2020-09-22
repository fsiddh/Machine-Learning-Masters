from wsgiref import simple_server
from flask import Flask, request
from flask import Response
import os
from flask_cors import CORS,cross_origin
import json

from com_in_ineuron_ai_prediction.predictApp import PredictApi
from com_in_ineuron_ai_training.trainApp import TrainApi
from com_in_ineuron_ai_utils.utils import createDirectoryForUser, extractDataFromTrainingIntoDictionary, \
    deleteExistingTrainingFolder

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)
# app.config['DEBUG'] = True

trainingDataFolderPath = "trainingData/"


class ClientApi:
    def __init__(self):
        stopWordsFilePath = "data/stopwords.txt"
        self.predictObj = PredictApi(stopWordsFilePath)
        self.trainObj = TrainApi(stopWordsFilePath)


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        if request.json['text'] is not None and request.json['userId'] is not None and request.json['projectId'] is not None:
            text = request.json['text']
            userId = str(request.json['userId'])
            projectId = str(request.json['projectId'])
            #csvFilePath = trainingData + userId + "/" + projectId + "/trainingData.csv"
            jsonFilePath = trainingDataFolderPath + userId + "/" + projectId + "/trainingData.json"
            modelPath = trainingDataFolderPath + userId + "/" + projectId + "/modelForPrediction.sav"
            vectorPath = trainingDataFolderPath + userId + "/" + projectId + "/vectorizer.pickle"
            result = clntApp.predictObj.executePreocessing(text, jsonFilePath,modelPath,vectorPath)


    except ValueError:
        return Response("Value not found inside  json trainingData")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        return Response((str(e)))
    return Response(result)


@app.route("/train", methods=['POST'])
@cross_origin()
def trainModel():

    try:
        if request.get_json() is not None:
            data = request.json['data']
        if request.json['userId'] is not None:
            userId = str(request.json['userId'])
            # path = trainingData+userId
        if request.json['projectId'] is not None:
            projectId = str(request.json['projectId'])
            # path = path + "/" + projectId
            #path = "C:\\Users\\user\\PycharmProjects\\TwitterSentimentAnalysis\\Twitter.json"

            createDirectoryForUser(userId, projectId)

        path = trainingDataFolderPath + userId + "/" + projectId

        trainingDataDict = extractDataFromTrainingIntoDictionary(data)

        with open(path + '/trainingData.json', 'w', encoding='utf-8') as f:
            json.dump(trainingDataDict, f, ensure_ascii=False, indent=4)
        #dataFrame = pd.read_json(path + '/trainingData.json')
        jsonpath = path + '/trainingData.json'
        modelPath = path
        modelscore = clntApp.trainObj.training_model(jsonpath,modelPath)
        #dataFrame.to_csv(path + '/trainingData.csv', index=None, header=True)
    except ValueError as val:
        return Response("Value not found inside  json trainingData", val)
    except KeyError as keyval:
        return Response("Key value error incorrect key passed", keyval)
    except Exception as e:
        return Response((str(e)))

    return Response("Success")


@app.route("/deleteuserproject", methods=["GET"])
@cross_origin()
def deleteUserProjectFolder():
    try:
        if request.args.get("userId") is not None:
            userIdAndProjectId = trainingDataFolderPath + request.args.get("userId")
        if request.args.get("projectId") is not None:
            userIdAndProjectId = userIdAndProjectId + "/" + request.args.get("projectId")

        # pathForExitingFolder = "ids/" + userId
        if userIdAndProjectId is not None:
            deleteExistingTrainingFolder(userIdAndProjectId)
        else:
            return Response("Please check your input")

    except Exception as e:
        return Response("Please check your input", e)
    return "Operation Successfully completed"


@app.route("/noofusers", methods=["GET"])
@cross_origin()
def getTrainingImagesFolders():
    try:
        for root, dirs, files in os.walk("trainingData"):
            print("%s these are the images you have trained so far" % dirs)
            return Response("%s these are the images you have trained so far" % dirs)
        return "We don't have any images for training so far"
    except Exception as e:
        return e
    return "We don't have any images for training so far"


port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clntApp = ClientApi()
    host = '0.0.0.0'
    #port = 5000
    httpd = simple_server.make_server(host, port, app)
    print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
# app.run(port=8080)

