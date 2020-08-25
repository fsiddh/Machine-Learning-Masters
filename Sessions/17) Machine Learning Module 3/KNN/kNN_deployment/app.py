import pickle
from flask import Flask, request, app
from flask import Response
from flask_cors import CORS
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

def predict_log(dict_pred):
    with open("standardScalar.sav", 'rb') as f:
        scalar = pickle.load(f)

    with open("modelForPrediction.sav", 'rb') as f:
        model = pickle.load(f)

    data_df = pd.DataFrame(dict_pred,index=[1,])
    scaled_data = scalar.transform(data_df)
    predict = model.predict(scaled_data)
    if predict[0] == 0:
        result = 'Non-Diabetic'
    else :
        result = 'Diabetic'

    return result


@app.route("/predict", methods=['POST'])
def predictRoute():
    try:
        if request.json['data'] is not None:
            data = request.json['data']
            print('data is:     ', data)
            res = predict_log(data)
            print('result is        ',res)
            return Response(res)
    except ValueError:
        return Response("Value not found")
    except Exception as e:
        print('exception is   ',e)
        return Response(e)


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(debug=True)
    #httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    #httpd.serve_forever()