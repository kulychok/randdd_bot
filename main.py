import telebot
import time
import languages as lg
import random
import telegram
import pymongo
import re
from telebot import types
import os
from flask import Flask, request
import logging

# telegram API token
bot = telebot.TeleBot('1099895310:AAHaLPowlJMPqGwsDwG27D45lvdqo8goNkw')
# server
server = Flask(__name__)

# mongodb token
random_bot_client = pymongo.MongoClient(
    'mongodb+srv://kulyk:c87hZXqIJEyz5LL5@cluster0-gqsxu.mongodb.net/test?retryWrites=true&w=majority'
)
database = random_bot_client.test
collection = database.users

digits_pattern = re.compile(r"^[0-9]+ [0-9]+$", re.MULTILINE)

numbers = [0, 0]
gifs = ['https://t.me/randchoosecont/80', 'https://t.me/randchoosecont/81']
lang_previous_message_id = 0
random_num_previous_message_id = 0


@bot.message_handler(commands=['start'])
def start_message(message):
    lg.language = lg.get_language(message.from_user.language_code)
    cursor = collection.find({"_id": message.from_user.id})
    for item in cursor:
        lg.language = item["lang_code"]
    choose_language(message)
    global lang_previous_message_id
    lang_previous_message_id = message.message_id


@bot.message_handler(commands=['help'])
def start_message(message):
    main_kb_update()
    bot.send_message(
        chat_id=message.chat.id,
        text=lg.help[lg.language],
        reply_markup=main_kb,
        parse_mode=telegram.ParseMode.MARKDOWN_V2
    )


# keyboards
main_kb = types.ReplyKeyboardMarkup(True)
rand_num_inline_kb = telebot.types.InlineKeyboardMarkup(True)
rand_num_chat_kb = types.InlineKeyboardMarkup(True)
coin_flip_inline_kb = telebot.types.InlineKeyboardMarkup(True)
coin_flip_chat_kb = types.InlineKeyboardMarkup(True)
language_kb = types.ReplyKeyboardMarkup(True)
language_kb.add(
    types.KeyboardButton('EN🇬🇧'),
    types.KeyboardButton('RU🇷🇺'),
    types.KeyboardButton('UA🇺🇦')
)


# keyboards' updates
def main_kb_update():
    global main_kb
    main_kb = types.ReplyKeyboardMarkup(True)
    main_kb.add(
        types.KeyboardButton(
            text=lg.coin_flipping_button[lg.language]
        ),
        types.KeyboardButton(
            text=lg.random_num[lg.language]
        )
    )
    main_kb.row(
        telebot.types.KeyboardButton(
            text=lg.switch_language[lg.language]
        )
    )


def rand_num_inline_kb_update():
    global rand_num_inline_kb
    rand_num_inline_kb = telebot.types.InlineKeyboardMarkup(True)
    rand_num_inline_kb.add(
        telebot.types.InlineKeyboardButton(
            text=lg.start_button[lg.language],
            callback_data="start_rand_nums"
        )
    )


def rand_num_chat_kb_update():
    global rand_num_chat_kb
    rand_num_chat_kb = types.InlineKeyboardMarkup(True)
    rand_num_chat_kb.add(
        types.InlineKeyboardButton(
            text=lg.start_button[lg.language],
            callback_data='start_rand_nums'
        ),
        types.InlineKeyboardButton(
            text=lg.forward_button[lg.language],
            switch_inline_query='{!s} {!s}'.format(numbers[0], numbers[1])
        )
    )


def coin_flip_inline_kb_update():
    global coin_flip_inline_kb
    coin_flip_inline_kb = telebot.types.InlineKeyboardMarkup(True)
    coin_flip_inline_kb.add(
        telebot.types.InlineKeyboardButton(
            text=lg.start_button[lg.language],
            callback_data="start_coin_flipping"
        )
    )


def coin_flip_chat_kb_update():
    global coin_flip_chat_kb
    coin_flip_chat_kb = types.InlineKeyboardMarkup(True)
    coin_flip_chat_kb.add(
        types.InlineKeyboardButton(
            text=lg.start_button[lg.language],
            callback_data='start_coin_flipping'
        ),
        types.InlineKeyboardButton(
            text=lg.forward_button[lg.language],
            switch_inline_query='c'
        )
    )


@bot.inline_handler(func=lambda query: len(query.query) is 0)
def empty_query(query):
    lg.language = find_language(query.from_user.id)
    inline_help = types.InlineQueryResultArticle(
        id='0',
        title=lg.help_title[lg.language],
        description=lg.help_description[lg.language],
        input_message_content=types.InputTextMessageContent(
            message_text=lg.help_message[lg.language],
            parse_mode=telegram.ParseMode.MARKDOWN_V2
        )
    )
    bot.answer_inline_query(query.id, [inline_help], cache_time=1)


# inline functions
@bot.inline_handler(func=lambda query: len(query.query) > 0)
def content_query(query):
    inline_coin_flipping(query)
    inline_random_number(query)


def inline_random_number(query):
    global numbers
    try:
        matches = re.search(digits_pattern, query.query)
    except AttributeError:
        return
    try:
        lg.language = find_language(query.from_user.id)
        numbers[0], numbers[1] = matches.group().split()
        if numbers[0] > numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0]
        rand_num_inline_kb_update()
        rand_nums = types.InlineQueryResultArticle(
            id="2",
            title=lg.random_num[lg.language],
            description=lg.borders[lg.language].format(numbers[0], numbers[1]),
            input_message_content=types.InputTextMessageContent(
                message_text=lg.random_num_inline_start[lg.language].format(numbers[0], numbers[1]),
                parse_mode=telegram.ParseMode.MARKDOWN_V2),
            reply_markup=rand_num_inline_kb,
        )
        bot.answer_inline_query(query.id, [rand_nums], cache_time=1)
    except Exception:
        pass


def inline_coin_flipping(query):
    lg.language = find_language(query.from_user.id)
    if query.query.lower() == 'c' or query.query.lower() == 'с':
        cf_img = "AgACAgIAAxkBAAMMXsGMo98G4qKKKji8dOKncgABIkk7AAJArjEbZxsJSoAjAwAB6dfQzUxoyw4ABAEAAwIAA20AA5nIBQABGQQ"
        coin_flip_inline_kb_update()
        coin_flipping = types.InlineQueryResultCachedPhoto(
            id="1",
            photo_file_id=cf_img,
            caption=lg.coin_flipping_inline_description[lg.language],
            reply_markup=coin_flip_inline_kb,
            parse_mode=telegram.ParseMode.MARKDOWN_V2
        )
        bot.answer_inline_query(query.id, [coin_flipping], cache_time=1)


# bot's chat functions
@bot.message_handler(content_types=['text'])
def menu(message):
    global random_num_previous_message_id
    lg.chooseLanguage(message.text)

    if message.text == lg.descriptions[lg.language]:
        try:
            name = "@" + message.from_user.username
        except AttributeError:
            name = "{!s} {!S}".format(message.from_user.first_name, message.from_user.last_name)
        try:
            set_language(message, name)
        except pymongo.errors.DuplicateKeyError:
            update_language(message)
        main_kb_update()
        if message.message_id - 2 == lang_previous_message_id:
            bot.send_message(message.chat.id, lg.wellcome[lg.language])
        bot.send_message(message.chat.id, lg.your_language[lg.language], reply_markup=main_kb)
    if message.text == lg.switch_language[lg.language]:
        choose_language(message)
        update_language(message)
    if message.text == lg.random_num[lg.language]:
        random_num_previous_message_id = message.message_id
        bot.send_message(
            chat_id=message.chat.id,
            text=lg.enter_borders[lg.language],
            parse_mode=telegram.ParseMode.MARKDOWN_V2
        )
    if message.text == lg.coin_flipping_button[lg.language]:
        coin_flip_chat_kb_update()
        bot.send_photo(
            chat_id=message.chat.id,
            photo='https://t.me/randchoosecont/82',
            caption=lg.coin_flipping_chat_description[lg.language],
            reply_markup=coin_flip_chat_kb,
            parse_mode=telegram.ParseMode.MARKDOWN_V2
        )
    if message.message_id - 2 == random_num_previous_message_id:
        chat_random_number(message)


def chat_random_number(message):
    global numbers
    try:
        matches = re.search(digits_pattern, message.text)
    except AttributeError:
        pass
    try:
        numbers[0], numbers[1] = matches.group().split()
        rand_num_chat_kb_update()
        bot.send_message(message.chat.id,
                         text=lg.random_num_chat_start[lg.language].format(numbers[0], numbers[1]),
                         reply_markup=rand_num_chat_kb,
                         parse_mode=telegram.ParseMode.MARKDOWN_V2)
    except AttributeError:
        if message.text != lg.coin_flipping_button[lg.language] \
                and message.text != lg.switch_language[lg.language]:
            bot.send_message(
                chat_id=message.chat.id,
                text=lg.incorrect_numbers[lg.language],
                parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
            global random_num_previous_message_id
            random_num_previous_message_id = message.message_id
        else:
            pass


def choose_language(message):
    bot.send_message(message.chat.id, lg.language_choose[lg.language], reply_markup=language_kb)


# callback function
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    result1 = str(random.randint(int(numbers[0]), int(numbers[1])))
    result = list(result1)
    emoji_result = []
    for res in result:
        emoji_result.append("{!s}️⃣".format(res))
    if call.message:
        if call.data == "start_rand_nums":
            main_kb_update()
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=lg.result[lg.language].format(numbers[0], numbers[1], ''.join(emoji_result)),
                parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=result1)
        if call.data == "start_coin_flipping":
            gif = random.choice(gifs)
            if gif == gifs[1]:
                word = lg.coin_flipping_head[lg.language]
            else:
                word = lg.coin_flipping_tail[lg.language]
            bot.edit_message_media(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                media=types.InputMediaAnimation(media=gif, caption="...")
            )
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
            time.sleep(4)
            bot.edit_message_media(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                media=types.InputMediaAnimation(media=gif, caption=word)
            )
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=word)
    elif call.inline_message_id:
        if call.data == "start_rand_nums":
            bot.edit_message_text(
                inline_message_id=call.inline_message_id,
                text=lg.result[lg.language].format(numbers[0], numbers[1], ''.join(emoji_result)),
                parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=result1)
        if call.data == "start_coin_flipping":
            gif = random.choice(gifs)
            if gif == gifs[1]:
                word = lg.coin_flipping_head[lg.language]
            else:
                word = lg.coin_flipping_tail[lg.language]
            bot.edit_message_media(
                inline_message_id=call.inline_message_id,
                media=types.InputMediaAnimation(media=gif, caption="...")
            )
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
            time.sleep(4)
            bot.edit_message_media(
                inline_message_id=call.inline_message_id,
                media=types.InputMediaAnimation(media=gif, caption=word)
            )
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=word)


# mongo functions
def set_language(message, name):
    collection.insert_one({
        "_id": message.from_user.id,
        "user_name": name,
        "lang_code": lg.language
    })


def update_language(message):
    collection.update_one(
        {
            "_id": message.from_user.id
        },
        {
            "$set": {
                "lang_code": lg.language
            }
        }
    )


def find_language(user_id):
    cursor = collection.find({"_id": user_id})
    for item in cursor:
        return item["lang_code"]


# webhook functions
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


@server.route('/1099895310:AAHaLPowlJMPqGwsDwG27D45lvdqo8goNkw', methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://randdd-bot.herokuapp.com/1099895310:AAHaLPowlJMPqGwsDwG27D45lvdqo8goNkw')
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
