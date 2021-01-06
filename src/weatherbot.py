import telegram as tg
import telegram.ext as tg_ext

from .weatherservice import WeatherService
from .replyformatter import ReplyFormatter


class WeatherBot:
    def __init__(self,
                 telegram_token: str,
                 openweather_token: str) -> None:
        self.__updater = tg_ext.Updater(token=telegram_token,
                                        use_context=True)
        self.__dispatcher = self.__updater.dispatcher
        self.__set_handlers()

        self.__weather = WeatherService(token=openweather_token)
        self.__reply_formatter = ReplyFormatter()

    def __set_handlers(self) -> None:
        self.__dispatcher.add_handler(tg_ext.MessageHandler(
            filters=tg_ext.Filters.text & ~tg_ext.Filters.command,
            callback=self.__send_weather_callback))

        self.__dispatcher.add_handler(tg_ext.CommandHandler(
            command='start', callback=self.__start_command_callback))

        self.__dispatcher.add_handler(tg_ext.CommandHandler(
            command='help', callback=self.__help_command_callback))


    def __help_command_callback(self, update: tg.Update, context: tg_ext.CallbackContext) -> None:
        user_id = update.message.chat.id

        reply = self.__reply_formatter.get_help_reply()

        self.__dispatcher.bot.send_message(chat_id=user_id, text=reply)

    def __send_weather_callback(self, update: tg.Update, context: tg_ext.CallbackContext) -> None:
        user_id = update.message.chat.id
        message_text = update.message.text

        try:
            city, weather = self.__weather.getCurrentWeather(message_text)
        except:
            reply = self.__reply_formatter.get_error_reply()
        else:
            reply = self.__reply_formatter.format_weather(city, weather)

        self.__dispatcher.bot.send_message(chat_id=user_id, text=reply)

    def __start_command_callback(self, update: tg.Update, context: tg_ext.CallbackContext) -> None:
        user_id = update.message.chat.id

        reply = self.__reply_formatter.get_start_reply()

        self.__dispatcher.bot.send_message(chat_id=user_id, text=reply)

    def start(self) -> None:
        self.__updater.start_polling()
        self.__updater.idle()

    def stop(self) -> None:
        self.__updater.stop()

