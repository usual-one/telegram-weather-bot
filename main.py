import os

import dotenv

from src.weatherbot import WeatherBot


def main() -> None:
    dotenv.load_dotenv()

    bot = WeatherBot(os.getenv('BOT_TOKEN'))
    bot.start()


if __name__ == '__main__':
    main()
