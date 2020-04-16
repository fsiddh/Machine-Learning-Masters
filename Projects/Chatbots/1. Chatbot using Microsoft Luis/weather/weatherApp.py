
import pyowm
from config.config_reader import ConfigReader

class WeatherInformation():
    def __init__(self):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()
        self.owmapikey = self.configuration['WEATHER_API_KEY']
        self.owm = pyowm.OWM(self.owmapikey)

    def get_weather_info(self,city):
        self.city=city

        # Here we are calling pre-defined method weather_at... from open weather map(owm)
        # which we subscribed to and we are using the key to connect to it and then proving city name.
        # Then the following codes we'll get different types of information.
        # And at last combine'em all.
        observation = self.owm.weather_at_place(city)
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
        self.bot_says = "Today the weather in " + city +" is :\n Maximum Temperature :"+temp_max_celsius+ " Degree Celsius"+".\n Minimum Temperature :"+temp_min_celsius+ " Degree Celsius" +": \n" + "Humidity :" + humidity + "%"
        return self.bot_says