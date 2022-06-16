# -*- coding: utf-8 -*-
import requests


API_KEY = '5bd4e284914842cd83f60840221705'
BASE_URL = 'http://api.weatherapi.com/v1/{type}?key={api_key}'


def get_current_weather(city):
    params = {'q': city}

    response = requests.get(
        BASE_URL.format(type='current.json', api_key=API_KEY),
        params
    ).json()

    return response
