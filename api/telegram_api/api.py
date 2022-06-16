# -*- coding: utf-8 -*-
import requests


SECRET_TOKEN = '5302136117:AAEH5BwYGraGLPX6jnRy6GuDHAM-mjSKDKw'
BASE_URL = f'https://api.telegram.org/bot{SECRET_TOKEN}/'


def get_updates():
    response = requests.get(BASE_URL + 'getUpdates')

    return response.json()


def send_message(chat_id, text, reply_markup=None):
    params = {
        'chat_id': chat_id,
        'text': text
    }

    if (reply_markup):
        params['reply_markup'] = reply_markup

    response = requests.post(BASE_URL + 'sendMessage', data=params)

    return response


# def set_my_commands(commands):
#     params = {'commands': commands}
#     response = requests.post(BASE_URL + 'setMyCommands', data=params)

#     return response


# def get_my_commands():
#     response = requests.post(BASE_URL + 'getMyCommands')

#     return response

# def send_poll(chat_id, question, options):
#     params = {
#         'chat_id': chat_id,
#         'question': question,
#         'options': options
#     }
#     response = requests.post(BASE_URL + 'sendPoll', data=params)

#     return response
