import telebot

bot = telebot.TeleBot("509161010:AAGcICZGPTiQTLJJJlScKszY5uUyo-bByuQ")



@bot.message_handler(commands=['start'])
def start_message(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/button')
    bot.send_message(message.from_user.id, "Привет, ткни в /button", reply_markup=user_markup)


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    Button1 = telebot.types.KeyboardButton("Кнопка1")
    Button2 = telebot.types.KeyboardButton("Кнопка2")
    markup.add(Button1)
    markup.add(Button2)
    bot.send_message(message.chat.id, 'Выбери тему', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    photoBug = open('C:/Photo/bug.jpg', 'rb')
    if message.text == "Кнопка1":
        bot.send_message(message.chat.id, 'Фоточка едет со стаффа')
        bot.send_photo(message.chat.id, 'https://staff.skbkontur.ru/api/images/291z79bp/qa.ke%20avatar%20small.png')
        bot.send_message(message.chat.id, 'Введи правильный ответ')
        if message.text.lower() == "Кнопка1": # Сообщение считывается только 1 раз, после чего идет вызов этой функции. Если нужно считать несколько раз, то надо как-то иначе колбасить
            bot.send_message(message.chat.id, message.from_user.username)
            # message.from_user.first_name - вариации данных от пользователя
            # message.from_user.last_name
            # message.from_user.username


    elif message.text == "Кнопка2":
        bot.send_message(message.chat.id, 'Фоточка едет локально с компа')
        bot.send_photo(message.chat.id, photoBug)

bot.polling(none_stop=True, interval=0)