#import config

import telebot
from telebot import types

global isSending
isSending = False

#bot = telebot.TeleBot(config.token)
bot = telebot.TeleBot('5222648948:AAGzwhD79ZBDAX6GxRiSlH_bwCwclHn9EAk')

@bot.message_handler(commands=['start'])
def welcome(message):
    lang_menu = types.ReplyKeyboardMarkup(True, True)
    item2 = types.KeyboardButton("Русский 🇷🇺")
    item3 = types.KeyboardButton("Украинский 🇺🇦")
    lang_menu.add(item2, item3)
    bot.send_message(message.chat.id, 'Выбери язык в меню'.format(
        message.from_user, bot.get_me()), parse_mode='html', reply_markup=lang_menu)

@bot.message_handler(commands=['send_query'])
def send_query_mode(message):
    global isSending
    isSending = True



@bot.message_handler(func = lambda message: message.text == "Русский 🇷🇺")
def russian(message):
    global rus_menu1
    rus_menu1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rus_menu1.add('Мне нужна помощь', 'Я хочу помочь',
                    'Оставить запрос', 'Назад')
    bot.send_message(
        message.chat.id, 'Вы выбрали русский язык. Выберите интересующую тему в меню.', reply_markup=rus_menu1)

# мне нужна помощь
@bot.message_handler(func = lambda message: message.text == "Мне нужна помощь")
def needhelp(message):
    rus_menu2 = types.ReplyKeyboardMarkup(True, True)
    rus_menu2.add('Я в Украине', 'Я в другой стране')
    bot.send_message(
        message.chat.id, 'Где вы находитесь?', reply_markup=rus_menu2)

# мне нужна помощь -> я в украине
@bot.message_handler(func = lambda message: message.text == "Я в Украине")
def needhelp_ua(message):
    global rus_menu3
    rus_menu3 = types.ReplyKeyboardMarkup(True, True)
    rus_menu3.add('Помощь по городам', 'Жильё', 'Гуманитарная помощь', 'Транспорт', 'Взаимопомощь')
    bot.send_message(message.chat.id, 'Выберите вид помощи в Украине', reply_markup=rus_menu3)

# мне нужна помощь -> я в украине -> по городам
@bot.message_handler(func = lambda message: message.text == "Помощь по городам")
def needhelp_ua_bycity(message):
    bot.send_message(message.chat.id, 'http://napryamok.org/ru#ukraine-cities', reply_markup=rus_menu3)

# мне нужна помощь -> я в украине -> жилье
@bot.message_handler(func = lambda message: message.text == "Жильё")
def needhelp_ua_housing(message):
    bot.send_message(message.chat.id, 'http://napryamok.org/ru#housing', reply_markup=rus_menu3)

# мне нужна помощь -> я в украине -> гуманитарная помощь
@bot.message_handler(func = lambda message: message.text == "Гуманитарная помощь")
def needhelp_ua_humanitarian(message):
    bot.send_message(message.chat.id, 'http://napryamok.org/ru#humanitarian-aid', reply_markup=rus_menu3)

# мне нужна помощь -> я в украине -> транспорт
@bot.message_handler(func = lambda message: message.text == "Транспорт")
def needhelp_ua_transport(message):
    bot.send_message(message.chat.id, 'http://napryamok.org/ru#refugees-transport', reply_markup=rus_menu3)

# мне нужна помощь -> я в украине -> взаимопомощь
@bot.message_handler(func = lambda message: message.text == "Взаимопомощь")
def needhelp_ua_help(message):
    bot.send_message(message.chat.id, 'http://napryamok.org/ru#help', reply_markup=rus_menu3)


# мне нужна помощь -> я в другой стране
@bot.message_handler(func = lambda message: message.text == "Я в другой стране")
def needhelp_elsewhere(message):
    rus_menu4 = types.ReplyKeyboardMarkup(True, True)
    rus_menu4.add('Страны, граничащие c Украиной', 'Остальные страны')
    bot.send_message(message.chat.id, 'Выберите вид помощи в Украине', reply_markup=rus_menu4)

# мне нужна помощь -> я в другой стране -> страны, граничащие с украиной
@bot.message_handler(func = lambda message: message.text == "Страны, граничащие c Украиной")
def needhelp_elsewhere_near(message):
    global rus_menu5
    rus_menu5 = types.ReplyKeyboardMarkup(True, True)
    rus_menu5.add('Венгрия', 'Польша', 'Румыния', 'Словакия', 'Молдова', 'Беларусь', 'Россия')
    bot.send_message(message.chat.id, 'Выберите страну, граничащую с Украиной', reply_markup=rus_menu5) 

# мне нужна помощь -> я в другой стране -> остальные страны
@bot.message_handler(func = lambda message: message.text == "Остальные страны")
def needhelp_elsewhere_else(message):
    bot.send_message(message.chat.id, 'http://napryamok.org/ru#other-countries')

@bot.message_handler(func = lambda message: message.text == "Венгрия")
def hungary(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/ru#hungary', reply_markup=rus_menu5)

@bot.message_handler(func = lambda message: message.text == "Польша")
def poland(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/ru#poland2', reply_markup=rus_menu5)

@bot.message_handler(func = lambda message: message.text == "Румыния")
def romania(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/ru#romania', reply_markup=rus_menu5)

@bot.message_handler(func = lambda message: message.text == "Словакия")
def slovakia(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/ru#slovakia', reply_markup=rus_menu5)

@bot.message_handler(func = lambda message: message.text == "Молдова")
def moldova(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/ru#moldova', reply_markup=rus_menu5)

@bot.message_handler(func = lambda message: message.text == "Беларусь")
def belarus(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/ru#belarus', reply_markup=rus_menu5)

@bot.message_handler(func = lambda message: message.text == "Россия")
def russia(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/ru#russia', reply_markup=rus_menu5)

##########

# я хочу помочь
@bot.message_handler(func = lambda message: message.text == "Я хочу помочь")
def wannahelp(message):
    global rus_menu6
    rus_menu6 = types.ReplyKeyboardMarkup(True, True)
    rus_menu6.add('В Украине', 'Из-за границы', 'Хочу добавить ресурс')
    bot.send_message(message.chat.id, 'Как вы хотите помочь?', reply_markup=rus_menu6)

# я хочу помочь -> в украине
@bot.message_handler(func = lambda message: message.text == "В Украине")
def wannahelp_ua(message):
    bot.send_message(message.chat.id, 'http://napryamok.org/ru#help-within', reply_markup=rus_menu6)

# я хочу помочь -> из-за границы
@bot.message_handler(func = lambda message: message.text == "Из-за границы")
def wannahelp_abroad(message):
    bot.send_message(message.chat.id, 'http://napryamok.org/#help-from-abroad', reply_markup=rus_menu6)

# я хочу помочь -> хочу добавить ресурс
@bot.message_handler(func = lambda message: message.text == "Хочу добавить ресурс")
def wannahelp_addresource(message):
    bot.send_message(message.chat.id, 'Пожалуйста, напишите нам на почту: team@napryamok.org (ответ в течение 48 часов) либо напишите ваше сообщение в чат', reply_markup=rus_menu6)
    # сделать пересыл сообщен

# оставить запрос
@bot.message_handler(func = lambda message: message.text == "Оставить запрос")
def query(message):
    #global rus_menu1
    bot.send_message(message.chat.id, '''Не нашли нужную информации?

Пожалуйста, воспользуйтесь поиском и изучите \
информацию на нашем сайте napryamok.org, возможно ответ есть там.

Если вы хотите сообщить об устаревшей и неактуальной информации, ошибках на сайте, у вас есть \
пожелания, предложения и идеи по улучшению сайта, если вы хотите помочь нам \
или у вас есть любые другие вопросы, пожалуйста, пишите нам на почту:\
team@napryamok.org (отвечаем в течение 48 часов).''', reply_markup=rus_menu1)

@bot.message_handler(func = lambda message: message.text == "Назад")
def r4(message):
    print(message.chat.id)

@bot.message_handler(func=lambda x: True)
def send_query(message):
    global isSending
    if isSending:
        bot.send_message(219449850, (message.json['from']['username'] + ':\n' + message.text))
        
        isSending = False


if __name__ == '__main__':
    bot.infinity_polling()