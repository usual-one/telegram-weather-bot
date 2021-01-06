class ReplyFormatter:
    def format_weather(self, city: str, weather) -> str:
        if weather is None:
            return self.get_error_reply()

        return f"Текущая погода в городе {city}:\n\n" +\
               f"{weather.detailed_status.capitalize()}\n" +\
               f"{weather.temperature('celsius')['temp']} °C"


    def get_error_reply(self) -> str:
        return 'Такого города не нашлось...'

    def get_help_reply(self) -> str:
        return 'Напишите город и я скажу текущую погоду в нем!'

    def get_start_reply(self) -> str:
        return 'Привет! Я Weather Bot! Напишите город и я скажу погоду в нем!'


