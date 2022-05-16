# -*- coding: utf-8 -*-
from time import sleep
import json
import api
import consts


def get_last_update(data):
    result = data['result']
    index = len(result) - 1

    return result[index]


def get_chat_id(update):
    chatId = update['message']['chat']['id']

    return chatId


def get_message_text(update):
    return update['message']['text']


# def init_commands():
#     commands = [
#         {
#             'command': 'useful_hint',
#             'description': 'get useful hint'
#         }, {
#             'command': 'bad_hint',
#             'description': 'get bad hint'
#         },
#     ]
#     api.set_my_commands(json.dumps(commands))


def init_keyboard(update):
    chatId = get_chat_id(update)

    keyboard_buttons = [[
        {
            'text': consts.KEYBOARD_BUTTONS['useful_hint']
        }, {
            'text': consts.KEYBOARD_BUTTONS['bad_hint']
        }
    ]]

    reply_markup = json.dumps({
        'keyboard':  keyboard_buttons
    })

    text = 'Choose, which hint you wanna get'

    response = api.send_message(chatId, text, reply_markup)
    
    return response.json()


def main():
    updates = api.get_updates()
    last_update = get_last_update(updates)
    last_update_id = last_update['update_id']
    chat_id = get_chat_id(last_update)

    init_keyboard(last_update)

    while True:
        updates = api.get_updates()
        last_update = get_last_update(updates)
        # print(json.dumps(last_update, indent=(2), ensure_ascii=False))
        
        if last_update_id == last_update['update_id']:
            message_text = get_message_text(last_update)
            
            if (message_text == consts.KEYBOARD_BUTTONS['useful_hint']):
                api.send_message(chat_id, 'USEFUL HINT')
                
            elif (message_text == consts.KEYBOARD_BUTTONS['bad_hint']):
                api.send_message(chat_id, 'BAD HINT')

            last_update_id += 1

        sleep(1)


if __name__ == '__main__':
    main()
