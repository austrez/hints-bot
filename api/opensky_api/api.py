# -*- coding: utf-8 -*-
import requests


API_KEY = '5bd4e284914842cd83f60840221705'
BASE_URL = 'https://opensky-network.org/api{type}'


def get_airport_arrivals(icao_code, begin_unix, end_unix):
    params = {
        'airport': icao_code,
        'begin': begin_unix,
        'end': end_unix
    }

    response = requests.get(
        BASE_URL.format(type='/flights/arrival'),
        params
    ).json()

    return response


def get_airport_departures(icao_code, begin_unix, end_unix):
    params = {
        'airport': icao_code,
        'begin': begin_unix,
        'end': end_unix
    }

    response = requests.get(
        BASE_URL.format(type='/flights/departure'),
        params
    ).json()

    return response
