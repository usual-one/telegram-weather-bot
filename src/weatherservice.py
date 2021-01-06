from pyowm.owm import OWM
from pyowm.utils import config


class WeatherService:
    def __init__(self, token):
        config_dict = config.get_default_config()
        config_dict['language'] = 'ru'

        self.__owm = OWM(api_key=token, config=config_dict)
        self.__weather_manager = self.__owm.weather_manager()

    def getCurrentWeather(self, city: str):
        weather = self.__weather_manager.weather_at_place(city)
        if weather is None:
            return city, None
        return weather.location.name, weather.weather

