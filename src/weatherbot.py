import telegram as tg
import telegram.ext as tg_ext


class WeatherBot:
    def __init__(self, token: str):
        self.__updater = tg_ext.Updater(token=token,
                                        use_context=True)
        self.__dispatcher = self.__updater.dispatcher

    def start(self):
        self.__updater.start_polling()
        self.__updater.idle()

    def stop(self):
        self.__updater.stop()

