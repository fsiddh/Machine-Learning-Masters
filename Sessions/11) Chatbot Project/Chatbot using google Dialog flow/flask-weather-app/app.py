from flask import Flask, request, make_response
import os, json
import pyowm
import os
from flask_cors import CORS,cross_origin

app = Flask(__name__)
# owmapikey=os.environ.get('119242c426975bc98ee4f259b9551823') #or provide your key here
owmapikey = '119242c426975bc98ee4f259b9551823'
owm = pyowm.OWM(owmapikey)


# geting and sending response to dialogflow
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req))

    res = processRequest(req)

    res = json.dumps(res)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


# processing the request from dialogflow
def processRequest(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    city = parameters.get("cityName")
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    latlon_res = observation.get_location()
    lat = str(latlon_res.get_lat())
    lon = str(latlon_res.get_lon())

    wind_res = w.get_wind()
    wind_speed = str(wind_res.get('speed'))

    humidity = str(w.get_humidity())

    celsius_result = w.get_temperature('celsius')
    temp_min_celsius = str(celsius_result.get('temp_min'))
    temp_max_celsius = str(celsius_result.get('temp_max'))

    fahrenheit_result = w.get_temperature('fahrenheit')
    temp_min_fahrenheit = str(fahrenheit_result.get('temp_min'))
    temp_max_fahrenheit = str(fahrenheit_result.get('temp_max'))
    speech = "Today the weather in " + city + ": \n" + "Humidity :" + humidity + ".\n Wind Speed :" + wind_speed

    return {
        "fulfillmentText": speech,
        "displayText": speech
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port)
