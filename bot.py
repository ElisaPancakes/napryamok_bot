import config

import telebot
from telebot import types

global isSending
isSending = False

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def welcome(message):
    lang_menu = types.ReplyKeyboardMarkup(True, True)
    item2 = types.KeyboardButton("Русский 🇷🇺")
    item3 = types.KeyboardButton("Украïнська 🇺🇦")
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
        message.chat.id, '''Приветствуем в napryamok_bot! 

Этот бот создан командой сайта информационной помощи napryamok.org. 

Здесь вы можете:

▫️ Получить информацию о получении помощи в Украине
▫️ Получить информацию о получении помощи в других странах
▫️ Узнать о возможностях волонтёрства  

Мы очень рекомендуем ознакомиться с ботом заранее – это может помочь в критической ситуации!''', reply_markup=rus_menu1)

# мне нужна помощь
@bot.message_handler(func = lambda message: message.text == "Мне нужна помощь")
def needhelp(message):
    rus_menu2 = types.ReplyKeyboardMarkup(True, True)
    rus_menu2.row('Я в Украине', 'Я в другой стране')
    rus_menu2.row('Назад')
    bot.send_message(
        message.chat.id, 'Где вы находитесь?', reply_markup=rus_menu2)

# мне нужна помощь -> я в украине
@bot.message_handler(func = lambda message: message.text == "Я в Украине")
def needhelp_ua(message):
    global rus_menu3
    rus_menu3 = types.ReplyKeyboardMarkup(True, True)
    rus_menu3.row('Помощь по городам', 'Жильё')
    rus_menu3.row('Гуманитарная помощь', 'Транспорт')
    rus_menu3.row('Взаимопомощь', 'Назад')


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
    rus_menu4.add('Страны, граничащие с Украиной', 'Остальные страны', 'Назад')
    bot.send_message(message.chat.id, 'Выберите вид помощи в Украине', reply_markup=rus_menu4)

# мне нужна помощь -> я в другой стране -> страны, граничащие с украиной
@bot.message_handler(func = lambda message: message.text == "Страны, граничащие с Украиной")
def needhelp_elsewhere_near(message):
    global rus_menu5
    rus_menu5 = types.ReplyKeyboardMarkup(True, True)
    rus_menu5.add('Венгрия', 'Польша', 'Румыния', 'Словакия', 'Молдова', 'Беларусь', 'Россия', 'Назад')

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
    rus_menu6.add('В Украине', 'Из-за границы', 'Хочу добавить ресурс', 'Назад')

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
    bot.send_message(message.chat.id, '''Пожалуйста, напишите нам на почту: team@napryamok.org либо отправьте сообщение с фразой "/send_query". 
    Следующее сообщение, которые вы введёте после "/send_query", будет отправлено нашей команде (ответ в течение 48 часов)''', reply_markup=rus_menu6)

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
def returning(message):
    welcome(message)
    






########### URKANIAN ################



@bot.message_handler(func = lambda message: message.text == "Украïнська 🇺🇦")
def ukranian(message):
    global ua_menu1
    ua_menu1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ua_menu1.add('Мені потрібна допомога', 'Я хочу допомогти','Залишити запит', 'Назад')

    bot.send_message(
        message.chat.id, '''Вітаємо в napryamok _ bot!

Цей бот створений командою сайту інформаційної допомоги napryamok.org. 

Тут ви можете: 

▫️ Отримати інформацію про отримання допомоги в Україні  
▫️ Отримати інформацію про отримання допомоги в інших країнах  
▫️ Дізнатися про можливості волонтерів   

Ми дуже рекомендуємо ознайомитися з ботом заздалегідь – це може допомогти в критичній ситуації!''', reply_markup=ua_menu1)

# мне нужна помощь
@bot.message_handler(func = lambda message: message.text == "Мені потрібна допомога")
def ua_needhelp(message):
    ua_menu2 = types.ReplyKeyboardMarkup(True, True)
    ua_menu2.row('Я в Україні', 'Я в іншій країні')
    ua_menu2.row('Назад')

    bot.send_message(
        message.chat.id, 'Де ви знаходитесь?', reply_markup=ua_menu2)

# мне нужна помощь -> я в украине
@bot.message_handler(func = lambda message: message.text == "Я в Україні")
def ua_needhelp_ua(message):
    global ua_menu3
    ua_menu3 = types.ReplyKeyboardMarkup(True, True)
    ua_menu3.row('Допомога у різних містах', 'Житло')
    ua_menu3.row('Гуманітарна допомога', 'Транспорт')
    ua_menu3.row('Взаємодопомога', 'Назад')

    bot.send_message(message.chat.id, 'Яка допомога вам потрібна?', reply_markup=ua_menu3)

# мне нужна помощь -> я в украине -> по городам
@bot.message_handler(func = lambda message: message.text == "Допомога у різних містах")
def ua_needhelp_ua_bycity(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#ukraine-cities', reply_markup=ua_menu3)

# мне нужна помощь -> я в украине -> жилье
@bot.message_handler(func = lambda message: message.text == "Житло")
def ua_needhelp_ua_housing(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#housing', reply_markup=ua_menu3)

# мне нужна помощь -> я в украине -> гуманитарная помощь
@bot.message_handler(func = lambda message: message.text == "Гуманітарна допомога")
def ua_needhelp_ua_humanitarian(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#humanitarian-aid', reply_markup=ua_menu3)

# мне нужна помощь -> я в украине -> транспорт
@bot.message_handler(func = lambda message: message.text == "Транспорт")
def ua_needhelp_ua_transport(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#refugees-transport', reply_markup=ua_menu3)

# мне нужна помощь -> я в украине -> взаимопомощь
@bot.message_handler(func = lambda message: message.text == "Взаємодопомога")
def ua_needhelp_ua_help(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#help', reply_markup=ua_menu3)


# мне нужна помощь -> я в другой стране
@bot.message_handler(func = lambda message: message.text == "Я в іншій країні")
def ua_needhelp_elsewhere(message):
    ua_menu4 = types.ReplyKeyboardMarkup(True, True)
    ua_menu4.row('Країни, що межують з Україною', 'Інші країни')
    ua_menu4.row('Назад')

    bot.send_message(message.chat.id, 'Яка допомога вам потрібна?', reply_markup=ua_menu4)

# мне нужна помощь -> я в другой стране -> Країни, що межують з Україною
@bot.message_handler(func = lambda message: message.text == "Країни, що межують з Україною")
def ua_needhelp_elsewhere_near(message):
    global ua_menu5
    ua_menu5 = types.ReplyKeyboardMarkup(True, True)
    ua_menu5.add('Угорщина', 'Польща', 'Румунія', 'Словаччина', 'Молдова', 'Білорусь', 'Росія', 'Назад')
    bot.send_message(message.chat.id, 'Выберите страну, граничащую с Украиной', reply_markup=ua_menu5) 

# мне нужна помощь -> я в другой стране -> Інші країни
@bot.message_handler(func = lambda message: message.text == "Інші країни")
def ua_needhelp_elsewhere_else(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#other-countries')

@bot.message_handler(func = lambda message: message.text == "Угорщина")
def ua_hungary(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#hungary', reply_markup=ua_menu5)

@bot.message_handler(func = lambda message: message.text == "Польща")
def ua_poland(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#poland2', reply_markup=ua_menu5)

@bot.message_handler(func = lambda message: message.text == "Румунія")
def ua_romania(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#romania', reply_markup=ua_menu5)

@bot.message_handler(func = lambda message: message.text == "Словаччина")
def ua_slovakia(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#slovakia', reply_markup=ua_menu5)

@bot.message_handler(func = lambda message: message.text == "Молдова")
def ua_moldova(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#moldova', reply_markup=ua_menu5)

@bot.message_handler(func = lambda message: message.text == "Білорусь")
def ua_belarus(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#belarus', reply_markup=ua_menu5)

@bot.message_handler(func = lambda message: message.text == "Росія")
def ua_russia(message):
    bot.send_message(message.chat.id, 'https://napryamok.org/#russia', reply_markup=ua_menu5)

##########

# я хочу помочь
@bot.message_handler(func = lambda message: message.text == "Я хочу допомогти")
def ua_wannahelp(message):
    global ua_menu6
    ua_menu6 = types.ReplyKeyboardMarkup(True, True)
    ua_menu6.add('В Україні', 'З-за кордону', 'Хочу додати ресурс', 'Назад')
    bot.send_message(message.chat.id, 'Як ви хочете допомогти?', reply_markup=ua_menu6)

# я хочу помочь -> в украине
@bot.message_handler(func = lambda message: message.text == "В Україні")
def ua_wannahelp_ua(message):
    bot.send_message(message.chat.id, 'http://napryamok.org/ru#help-within', reply_markup=ua_menu6)

# я хочу помочь -> З-за кордону
@bot.message_handler(func = lambda message: message.text == "З-за кордону")
def ua_wannahelp_abroad(message):
    bot.send_message(message.chat.id, 'http://napryamok.org/#help-from-abroad', reply_markup=ua_menu6)

# я хочу помочь -> Хочу додати ресурс
@bot.message_handler(func = lambda message: message.text == "Хочу додати ресурс")
def ua_wannahelp_addresource(message):
    bot.send_message(message.chat.id, '''Будь ласка, напишіть нам на пошту: team@napryamok.org або надішліть повідомлення із фразою "/send_query".
Наступне повідомлення, яке ви введете після "/send_query", буде надіслано нашій команді (відповідь протягом 48 годин)''', reply_markup=ua_menu6)

# оставить запрос
@bot.message_handler(func = lambda message: message.text == "Залишити запит")
def ua_query(message):
    #global ua_menu1
    bot.send_message(message.chat.id, '''Не знайшли потрібну інформації?

Будь ласка, скористайтеся пошуком і вивчіть інформацію на нашому сайті napryamok.org, \
можливо відповідь є там. 

Якщо ви хочете повідомити про застарілу і неактуальну інформацію, \
помилки на сайті, у вас є побажання, пропозиції і ідеї по поліпшенню сайту, \
якщо ви хочете допомогти нам або у вас є будь-які інші питання, будь ласка, \
пишіть нам на пошту: team@napryamok.org (відповідаємо впродовж 48 годин).  ''', reply_markup=ua_menu1)


    






@bot.message_handler(func=lambda x: True)
def send_query(message):
    global isSending
    if isSending:
        bot.send_message(config.queryto_id, (message.json['from']['username'] + ':\n' + message.text))
        
        isSending = False


if __name__ == '__main__':
    bot.infinity_polling()