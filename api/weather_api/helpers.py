import random

from . import api


CITIES = (
    'London',
    'Moscow',
    'Tokyo',
    'Saint-Petersburg',
    'Paris',
    'New York',
    'Sochi',
    'Bangkok',
    'Hong Kong',
    'Dubai'
)


def get_current_weather():
    city = random.choice(CITIES)
    response = api.get_current_weather(city)

    city = response['location']['name']
    condition = response['current']['condition']['text']

    weather = f'The weather in {city} {condition}!'

    return weather
