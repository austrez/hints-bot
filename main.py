# -*- coding: utf-8 -*-
from time import sleep

import json
import pathlib
import random

import api.telegram_api.helpers as telegram
import api.weather_api.helpers as weather
import api.opensky_api.helpers as opensky
import api.travelpayouts_api.helpers as travelpayouts

import consts


CURRENT_DIR = str(pathlib.Path(__file__).parent.resolve())


def load_free_hints():
    free_hints = None
    full_path = CURRENT_DIR + '\\data\\free_hints.json'

    with open(full_path, 'r', encoding='utf-8') as f:
        free_hints = json.load(f)
        f.close()

    return free_hints


def load_paid_hint():
    api_name = random.choice(list(consts.api_names.keys()))
    print(api_name)
    hint = None

    if (api_name == consts.api_names['weather_api']):
        hint = weather.get_current_weather()

    elif (api_name == consts.api_names['opensky_api']):
        hint = opensky.load_flights_history()

    elif (api_name == consts.api_names['travelpayouts_api']):
        hint = travelpayouts.get_trips_schedule()

    return hint


def main():
    updates = telegram.get_updates()
    last_update = telegram.get_last_update(updates)
    last_update_id = last_update['update_id']
    chat_id = telegram.get_chat_id(last_update)

    free_hints = load_free_hints()

    telegram.init_keyboard(chat_id)

    while True:
        updates = telegram.get_updates()
        last_update = telegram.get_last_update(updates)
        # print(json.dumps(last_update, indent=(2), ensure_ascii=False))

        if (last_update_id == last_update['update_id']):
            message_text = telegram.get_message_text(last_update)

            # If the user has chosen "paid hint" then
            # we send data from one of the three APIs
            if (message_text == telegram.KEYBOARD_BUTTONS['paid_hint']):
                paid_hint = load_paid_hint()

                telegram.send_message(chat_id, paid_hint)
                last_update_id += 1

            # If the user has chosen "free hint" then
            # we send data from static json file
            elif (message_text == telegram.KEYBOARD_BUTTONS['free_hint']):
                random_hint = random.choice(free_hints)
                telegram.send_message(chat_id, random_hint)
                last_update_id += 1

        sleep(1)


if __name__ == '__main__':
    main()
