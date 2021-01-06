# Weather telegram bot

Simple telegram bot telling current weather for BMSTU APL course.

## Used languages and libraries

Languages:
- Python 3

Libraries:
- python-telegram-bot
- pyowm

## Installation

Set virtual environment inside root folder:
```sh
$ python3 -m venv .venv
$ source ./venv/bin/activate
$ pip3 install -r requirements.txt
```

Set environmental variables inside `.env` file (you need to create it):
```sh
TELEGRAM_TOKEN=your-telegram-bot-token
OPENWEATHER_TOKEN=your-open-weather-api-key
```

## Starting

To start:
```sh
$ python3 main.py
```
