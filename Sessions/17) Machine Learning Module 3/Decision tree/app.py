import pickle
from wsgiref import simple_server
from flask import Flask, request, app
from flask import Response
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True



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

def predict_log(dict_pred):
    with open("standardScalar.sav", 'rb') as f:
        scalar = pickle.load(f)

    with open("modelForPrediction.sav", 'rb') as f:
        model = pickle.load(f)
    with open("pca_model.sav", 'rb') as f:
        pca_model = pickle.load(f)

    data_df = pd.DataFrame(dict_pred,index=[1,])
    scaled_data = scalar.transform(data_df)
    principal_data = pca_model.transform(scaled_data)
    predict = model.predict(principal_data)
    if predict[0] == 3:
        result = 'Bad'
    elif predict[0] == 4 :
        result = 'Below Average'
    elif predict[0]==5:
        result = 'Average'
    elif predict[0] == 6:
        result = 'Good'
    elif predict[0] == 7:
        result = 'Very Good'
    else :
        result = 'Excellent'

    return result
if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(debug=True)
    #httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    #httpd.serve_forever()