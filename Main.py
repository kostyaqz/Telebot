import SqlBase
import sqlite3
import telebot

bot = telebot.TeleBot("509161010:AAGcICZGPTiQTLJJJlScKszY5uUyo-bByuQ")
db = sqlite3.connect('server.db', check_same_thread=False)

# ВОТ ЭТО НУЖНО УДАЛИТЬ ОБЯЗАТЕЛЬНО
#to do

SqlBase.DataBase.SelectFromDataBase(db)


#SqlBase.DataBase.DropDataBase(sql,db)
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
        for value in SqlBase.DataBase.ViewLeaderBoard(db):
            bot.send_message(message.chat.id, value)
    else:
        bot.send_message(message.chat.id, 'В любой непонятной ситуации жми /start')


def AnswerValidator(message, nextRebus):

    print('Второй этап запустился')
    print(SqlBase.DataBase.SelectCorrectAnswer(db, nextRebus))

    if message.text.lower() == SqlBase.DataBase.SelectCorrectAnswer(db, nextRebus):
        SqlBase.DataBase.AddPoints(db, message.from_user.username, nextRebus)
        bot.send_message(message.chat.id, 'Это правильный ответ')
        bot.send_message(message.chat.id, 'Следующий ребус')
        SentNextRebus(message, db)
    elif message.text == "Список лидеров":
        for value in SqlBase.DataBase.ViewLeaderBoard(db):
            bot.send_message(message.chat.id, value)
    else:
        bot.send_message(message.chat.id, 'Нет, это неправильный ответ')
        bot.send_message(message.chat.id, 'Следующий ребус')
        SentNextRebus(message, db)




def SentNextRebus(message, db):
    nextRebus = SqlBase.DataBase.NextRebus(message.from_user.username, db)
    bot.send_photo(message.chat.id, nextRebus)
    msg = bot.send_message(message.chat.id, 'Введи правильный ответ по русски')

    bot.register_next_step_handler(msg, AnswerValidator, nextRebus)


bot.polling(none_stop=True, interval=0)