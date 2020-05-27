import os, json
import pyowm
from flask import Flask, request, make_response
from flask_cors import cross_origin

app = Flask(__name__)
owmapikey = '0c3dd17815f8c950ea58b580714c102c'
owm = pyowm.OWM(owmapikey)


@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)

    res = processrequest(req)
    res = json.dump(res)

    # Just to convert it in a form of Web API
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processrequest(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    city = parameters.get("cityName")

    # Through this you get the google Dialogflow API response structure
    # It gives us details of the weather in 'city' 
    observation = owm.weather_at_place(city)

    w = observation.get_weather()
    latlon = observation.get_location()

    lat = str(latlon.get_lat())
    lon = str(latlon.get_lon())

    humidity = str(w.get_humidity())

    temp_celsius = w.get_temperature('celsius')
    temp_min_celsius = str(temp_celsius.get('temp_min'))
    temp_max_celsius = str(temp_celsius.get('temp_max'))

    wind = w.get_wind()
    wind_speed = str(wind.get('speed'))

    speech = "Today the weather in " + city + ": \n" + "Humidity :" + humidity + ".\n Wind Speed :" + wind_speed

    return {
        "fulfillmentText": speech
    }


if __name__ == '__main__':
    app.run()