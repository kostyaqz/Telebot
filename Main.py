import SqlBase
import sqlite3
import telebot


bot = telebot.TeleBot("509161010:AAGcICZGPTiQTLJJJlScKszY5uUyo-bByuQ")
db = sqlite3.connect('server.db', check_same_thread=False)
sql = db.cursor()

# ВОТ ЭТО НУЖНО УДАЛИТЬ ОБЯЗАТЕЛЬНО
#to do
SqlBase.DataBase.DropDataBase(sql,db)
print('УДАЛИ ЭТО ОБЯЗАТЕЛЬНО')

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    rebus = telebot.types.KeyboardButton("Играть")
    liderBoard = telebot.types.KeyboardButton("Список лидеров")

    SqlBase.DataBase.CreateDataBase(sql, db)
    SqlBase.DataBase.InsertNewUser(message.from_user.username, sql, db)

    markup.add(rebus)
    markup.add(liderBoard)

    bot.send_message(message.chat.id, 'Выбери тему', reply_markup=markup)



@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Играть":
        SentNextRebus(message, sql)


def AnswerValidator(message, nextRebus):

    print('Второй этап запустился')
    print(SqlBase.DataBase.SelectCorrectAnswer(db, nextRebus))

    if message.text.lower() == SqlBase.DataBase.SelectCorrectAnswer(db, nextRebus):
        SqlBase.DataBase.AddPoints(sql, message.from_user.username, nextRebus)
        bot.send_message(message.chat.id, 'Это правильный ответ')
    else:
        bot.send_message(message.chat.id, 'Нет, это неправильный ответ')

    bot.send_message(message.chat.id, 'Следующий ребус')
    SentNextRebus(message, sql)


def SentNextRebus(message, sql):
    nextRebus = SqlBase.DataBase.NextRebus(message.from_user.username, sql)
    bot.send_photo(message.chat.id, nextRebus)
    msg = bot.send_message(message.chat.id, 'Введи правильный ответ по русски')

    bot.register_next_step_handler(msg, AnswerValidator, nextRebus)


bot.polling(none_stop=True, interval=0)