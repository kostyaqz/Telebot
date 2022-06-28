import SqlBase
import sqlite3
import telebot

bot = telebot.TeleBot("5546767894:AAH8HAnbEJdJmLxRl6STgQK6R3d-k2_0rdE")
db = sqlite3.connect('server.db', check_same_thread=False)

# ВОТ ЭТО НУЖНО УДАЛИТЬ ОБЯЗАТЕЛЬНО
#to do

SqlBase.DataBase.DropDataBase(db)
print('УДАЛИ ЭТО ОБЯЗАТЕЛЬНО')

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    rebus = telebot.types.KeyboardButton("Играть")
    liderBoard = telebot.types.KeyboardButton("Список лидеров")

    SqlBase.DataBase.CreateDataBase(db)
    SqlBase.DataBase.InsertNewUser(message.from_user.username, db)

    markup.add(rebus)
    markup.add(liderBoard)

    bot.send_message(message.chat.id, 'Тыкай по кнопке', reply_markup=markup)



@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Играть":
        SentNextRebus(message, db)
    elif message.text == "Список лидеров":
        ViewLeaderBoard(db, message)
    else:
        bot.send_message(message.chat.id, 'В любой непонятной ситуации жми /start')


def AnswerValidator(message, nextRebus):

    if message.text.lower() == SqlBase.DataBase.SelectCorrectAnswer(db, nextRebus):
        SqlBase.DataBase.AddPoints(db, message.from_user.username, nextRebus)
        bot.send_message(message.chat.id, 'Это правильный ответ')
        bot.send_message(message.chat.id, 'Следующий ребус')
        SentNextRebus(message, db)
    elif message.text == "Список лидеров":
        ViewLeaderBoard(db, message)
    else:
        bot.send_message(message.chat.id, 'Нет, это неправильный ответ')
        bot.send_message(message.chat.id, 'Следующий ребус')
        SentNextRebus(message, db)


def SentNextRebus(message, db):
    nextRebus = SqlBase.DataBase.NextRebus(message.from_user.username, db)
    if nextRebus != '':
        bot.send_photo(message.chat.id, nextRebus)
        msg = bot.send_message(message.chat.id, 'Введи правильный ответ по русски')

        bot.register_next_step_handler(msg, AnswerValidator, nextRebus)
    else:
        bot.send_message(message.chat.id, 'Поздравляю, все ребусы пройдены')
        ViewLeaderBoard(db, message)


def ViewLeaderBoard(db, message):
    for value in SqlBase.DataBase.SelectLeaderBoard(db):
        msg = str(value)
        bot.send_message(message.chat.id, msg)

bot.polling(none_stop=True, interval=0)