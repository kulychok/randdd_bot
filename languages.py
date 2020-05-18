language = 'en'


def get_language(lang_code):
    if not lang_code:
        return 'en'
    if '-' in lang_code:
        lang_code = lang_code.split("-")[0]
    if lang_code == 'ru':
        return 'ru'
    if lang_code == 'uk':
        return 'ua'
    else:
        return 'en'


def chooseLanguage(message):
    global language
    if message == 'EN🇬🇧':
        language = 'en'
    elif message == 'RU🇷🇺':
        language = 'ru'
    elif message == 'UA🇺🇦':
        language = 'ua'


help = {'en': '''*Bot's actions in bot's chat:* 
  1\) Use button __Coin flipping__ to random get head or tail
  2\) Use button __Random number__ to get a random number in your borders
  3\) Use button __Switch language__ to choose another language
*Bot's actions in any chats:*
  1\) Type "`@randdd\_bot c`" and press on prompt to random get head or tail
  2\) Type "`@randdd\_bot n1 n2`", and press on prompt to get a random number in your borders, where n1,n2 \- your borders of random''',
        'ru': '''*Действия бота в собственном чате:* 
  1\) Используйте кнопку __Орёл или решка__ что бы случайно получить орла или решку
  2\) Используйте кнопку __Случайное число__ что бы получить случайное чисто в заданных границах
  3\) Используйте кнопку __Изменить язык__ что бы изменить язык
*Действия бота в любом чате:*
  1\) Пишите "`@randdd\_bot c`" и нажмите на подсказку что бы случайно получить орла или решку
  2\) Пишите "`@randdd\_bot n1 n2`", и нажмите на подсказку что бы получить случайное чисто в заданных границах, где n1,n2 \- ваши границы допустимого числа''',
        'ua': '''*Дії бота у своєму чаті:*
  1\) Натисніть кнопку __Орел або решка__ щоб отримати орла або решку випадковим чином
  2\) Натисніть кнопку __Випадкове число__ щоб отримати випадкове число у заданих границях
  3\) Натисніть кнопку __Змінити мову__ щоб змінити мову
*Дії бота у будь\-якому чаті:*
  1\) Пишіть "`@randdd\_bot c`" і натисніть на підказку щоб отримати орла або решку випадковим чином
  2\) Пишіть "`@randdd\_bot n1 n2`", і натисніть на підказку щоб отримати випадкове чисто в заданих границях, де n1,n2 \- ваші границі допустимого числа'''}
switch_language = {'en': "Switch language",
                   'ru': "Изменить язык",
                   'ua': "Змінити мову"}
language_choose = {'en': "Choose your language:",
                   'ru': "Выберите ваш язык:",
                   'ua': "Оберіть вашу мову:"}
descriptions = {'en': 'EN🇬🇧', 'ru': 'RU🇷🇺', 'ua': 'UA🇺🇦'}

wellcome = {
    'en': 'Wellcome!',
    'ru': "Добро пожаловать!",
    'ua': 'Вітаю!'
}

your_language = {
    'en': "You have chosen English. You can always change it",
    'ru': "Вы выбрали русский язык. Вы всегда можете изменить его",
    'ua': "Ви вибрали українську мову. Ви завжди можете змінити її"
}

random_num = {'en': 'Random number', 'ru': 'Случайное число', 'ua': 'Випадкове число'}
enter_borders = {
    'en': "Enter the borders separated by space, for example: `1 10`",
    'ru': "Введите границы числа через пробел, например: `1 10`",
    'ua': "Введіть границі числа через пробіл, например `1 10`:"
}
borders = {'en': "From {!s} to {!s}", 'ru': "От {!s} до {!s}", 'ua': "Від {!s} до {!s}"}
random_num_inline_start = {
    'en': "Press __Start__ to run random from *{!s}* to *{!s}*",
    'ru': "Нажмите __Старт__ что бы получить случайное число от *{!s}* до *{!s}*",
    'ua': "Натисніть __Старт__ щоб отримати випадкове число від *{!s}* до *{!s}*"
}
random_num_chat_start = {
    'en': "Press __Start__ to run random from *{!s}* to *{!s}* or __Forward__ to get random number in any chat",
    'ru': "Нажмите __Старт__ что бы получить случайное число от *{!s}* до *{!s}*, или __Переслать__ что бы получить "
          "случайное число в другом чате",
    'ua': "Натисніть __Старт__ щоб отримати випадкове число від *{!s}* до *{!s}*, або __Переслати__ щоб отримати "
          "випадкове число в іншому чаті"
}
help_title = {'en': "Available actions", 'ru': "Доступные действия", 'ua': "Доступні дії"}
help_description = {
    'en': "Press here to see bot's actions",
    'ru': "Нажмите сюда что бы увидеть доступные действия",
    'ua': "Натисніть сюди щоб побачити доступні дії"
}
help_message = {'en': '''*Bot's actions in any chats:*
  1\) Type "`@randdd\_bot c`" and press on prompt to random get head or tail
  2\) Type "`@randdd\_bot n1 n2`", and press on prompt to get a random number in your borders, where n1,n2 \- your borders of random''',
                'ru': '''*Действия бота в любом чате:*
  1\) Пишите "`@randdd\_bot c`" и нажмите на подсказку что бы случайно получить орла или решку
  2\) Пишите "`@randdd\_bot n1 n2`", и нажмите на подсказку что бы получить случайное чисто в заданных границах, где n1,n2 \- ваши границы допустимого числа''',
                'ua': '''*Дії бота у будь\-якому чаті:*
  1\) Пишіть "`@randdd\_bot c`" і натисніть на підказку щоб отримати орла або решку випадковим чином
  2\) Пишіть "`@randdd\_bot n1 n2`", і натисніть на підказку щоб отримати випадкове чисто в заданих границях, де n1,n2 \- ваші границі допустимого числа'''}

start_button = {'en': "Start", 'ru': "Старт", 'ua': "Старт"}
forward_button = {'en': "Forward", 'ru': "Переслать", 'ua': "Переслати"}
result = {'en': "Result of random:\n_from_ *{!s}*\n_to_ *{!s}*\n_is_ {!s}",
          'ru': "Результат выбора случайного числа:\n_от_ *{!s}*\n_до_ *{!s}*\n_равен_  {!s}",
          'ua': "Результат вибору випадкового числа:\n_від_ *{!s}*\n_до_ *{!s}*\n_дорівнює_ {!s}"}
coin_flipping_button = {'en': 'Heads or tails', 'ru': 'Орёл или решка', 'ua': 'Орел або решка'}
coin_flipping_inline_description = {'en': "Press __Start__ to run _Coin flipping_",
                                    'ru': "Нажмите __Старт__ что бы запустить _Орёл или решка_",
                                    'ua': "Натисніть __Старт__ щоб запустити _Орел або решка_"}
coin_flipping_chat_description = {
    'en': "Press __Start__ to run _Coin flipping_ or __Forward__ to use _Coin flipping_ in any chat",
    'ru': "Нажмите __Старт__ что бы запустить _Орёл или решка_, или __Переслать__ что бы использовать _Орёл или "
          "решка_ в другом чате",
    'ua': "Натисніть __Старт__ щоб запустити _Орел або решка_, або __Переслати__ щоб використати _Орел або решка_ в "
          "іншому чаті "
}
coin_flipping_head = {'en': "Head", 'ru': "Орёл", 'ua': "Орел"}
coin_flipping_tail = {'en': "Tail", 'ru': "Решка", 'ua': "Решка"}

incorrect_numbers = {'en': "Numbers entered incorrectly\!\nEnter integers, for example: `1 10`",
                     'ru': "Числа введены некорректно\!\nВведите целые числа, например: `1 10`",
                     'ua': "Числа введені некоректно\!\nВведіть цілі числа, наприклад: `1 10`"}

emojis = list('😀😃😄😁😆😅😂🤣☺😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩🥳😏😒😞😔😟😕🙁☹'
              '😣😖😫😩🥺😢😭😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲🥱😴🤤😪'
              '😵🤐🥴🤮🤧😷🤒🤕🤑🤠😈👿💩')

too_large_number = {
    'en': "Too large number!",
    'ru': "Слишком большое число!",
    'ua': "Занадто велике число!"
}
