# -*- coding: utf-8 -*-
import requests
import json

BASE_URL = 'https://suggest.travelpayouts.com/search?service=tutu_trains'


def get_trips_schedule(departure_code, arrival_code):
    params = {
        "term": departure_code,
        "term2": arrival_code,
    }

    response = requests.get(
        BASE_URL,
        params
    ).json()

    print(json.dumps(response, indent=(2), ensure_ascii=False))

    return response
