# -*- coding: utf-8 -*-
import json

from . import api

KEYBOARD_BUTTONS = {
    'paid_hint': 'paid hint',
    'free_hint': 'free hint'
}


def get_updates():
    return api.get_updates()


def get_last_update(data):
    result = data['result']
    index = len(result) - 1

    return result[index]


def get_chat_id(update):
    chatId = update['message']['chat']['id']

    return chatId


def get_message_text(update):
    return update['message']['text']


def send_message(chat_id, text):
    response = api.send_message(chat_id, text)

    return response


def init_keyboard(chat_id):
    keyboard_buttons = [[
        {
            'text': KEYBOARD_BUTTONS['paid_hint']
        }, {
            'text': KEYBOARD_BUTTONS['free_hint']
        }
    ]]

    reply_markup = json.dumps({
        'keyboard':  keyboard_buttons
    })

    text = 'Choose, which hint you wanna get'

    response = api.send_message(chat_id, text, reply_markup)

    return response.json()
