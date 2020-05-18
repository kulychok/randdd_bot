import languages as lg
import telebot
from main import nums

# keyboards:
# main keyboard
action_keyboard = telebot.types.ReplyKeyboardMarkup(True)
action_keyboard.add(
    telebot.types.KeyboardButton(
        text=lg.coin_flipping_button[lg.language]
    ),
    telebot.types.KeyboardButton(
        text=lg.random_num[lg.language]
    )
)
action_keyboard.row(
    telebot.types.KeyboardButton(
        text=lg.switch_language[lg.language]
    )
)

# language keyboard
language_kb = telebot.types.ReplyKeyboardMarkup(True)
language_kb.add(
    telebot.types.KeyboardButton('EN🇬🇧'),
    telebot.types.KeyboardButton('RU🇷🇺'),
    telebot.types.KeyboardButton('UA🇺🇦')
)

# random numbers keyboards
rand_num_inline_kb = telebot.types.InlineKeyboardMarkup(True)
rand_num_inline_kb.add(
    telebot.types.InlineKeyboardButton(
        text=lg.start_button[lg.language],
        callback_data="start_nums"
    )
)

rand_num_chat_kb = telebot.types.InlineKeyboardMarkup(True)
rand_num_chat_kb.add(
    telebot.types.InlineKeyboardButton(
        text=lg.start_button[lg.language],
        callback_data='start_nums'
    ),
    telebot.types.InlineKeyboardButton(
        text=lg.forward_button[lg.language],
        switch_inline_query='{!s} {!s}'.format(numbers[0], numbers[1])
    )
)

# coin flipping keyboards
coin_flip_chat_kb = telebot.types.InlineKeyboardMarkup(True)
coin_flip_chat_kb.add(
    telebot.types.InlineKeyboardButton(
        text=lg.start_button[lg.language],
        callback_data="start_HOT"
    )
)

coin_flip_inline_kb = telebot.types.InlineKeyboardMarkup(True)
coin_flip_inline_kb.add(
    telebot.types.InlineKeyboardButton(
        text=lg.start_button[lg.language],
        callback_data='start_HOT'
    ),
    telebot.types.InlineKeyboardButton(
        text=lg.forward_button[lg.language],
        switch_inline_query='c'
    )
)