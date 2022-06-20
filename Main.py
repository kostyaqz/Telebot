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

# И нужны методы обвязки, которые будут включать в себя бота и команды SQL
#Бота надо как-то растащить на методы




#первое действие человека, который зашел в бота
@bot.message_handler(commands=['start'])
def start_message(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    SqlBase.DataBase.CreateDataBase(sql, db)
    SqlBase.DataBase.InsertNewUser(message.from_user.username, sql, db)

    SqlBase.DataBase.SelectFromDataBase(sql)
    user_markup.row('/button')
    bot.send_message(message.from_user.id, "Привет, ткни в /button", reply_markup=user_markup)






#Рисует кнопки
@bot.message_handler(commands=['button'])
def button_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    rebus = telebot.types.KeyboardButton("Ребус")
    Button2 = telebot.types.KeyboardButton("Кнопка2")
    markup.add(rebus)
    markup.add(Button2)
    bot.send_message(message.chat.id, 'Выбери тему', reply_markup=markup)




#Реагирует на кнопки
#По клику на "Кнопка1" вызывает рандомную картинку из базы
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Ребус":
        nextRebus = SqlBase.DataBase.NextRebus(message.from_user.username, sql)
        bot.send_message(message.chat.id, 'Фоточка грузится')
        bot.send_photo(message.chat.id, nextRebus)
        msg = bot.send_message(message.chat.id, 'Введи правильный ответ по русски')

        bot.register_next_step_handler(msg, after_text_2, nextRebus)
    #elif message.text == "Исключи лишнее":
        #Заглушка
    #else
        #bot.send_message(message.chat.id, 'Таких вариантов у меня нет, попробуй еще')







def after_text_2(message, nextRebus):

    print('Второй этап запустился')
    #correctAnswer = SqlBase.DataBase.SelectCorrectAnswer(sql, nextRebus)

    print(SqlBase.DataBase.SelectCorrectAnswer(db, nextRebus))
    #if message.text.lower() == correctAnswer:
    if message.text.lower() == SqlBase.DataBase.SelectCorrectAnswer(db, nextRebus):
        bot.send_message(message.chat.id, 'Это правильный ответ')
        SqlBase.DataBase.AddPoints(sql, message.from_user.username, nextRebus)
        msg = bot.send_message(message.chat.id, 'Следующий ребус')
        RebusCycle(message, sql)




        # bot.register_next_step_handler(msg, after_text_2, SqlBase.DataBase.NextRebus(message.from_user.username, sql))
    else:
        bot.send_message(message.chat.id, 'Нет, это неправильный ответ')
        bot.send_message(message.chat.id, 'Ребус')
        bot.send_message(message.chat.id, 'Следующий ребус')
        RebusCycle(message, sql)

        #bot.register_next_step_handler(msg, after_text_2, SqlBase.DataBase.NextRebus(message.from_user.username, sql))





def RebusCycle(message, sql):
    nextRebus = SqlBase.DataBase.NextRebus(message.from_user.username, sql)
    bot.send_message(message.chat.id, 'Фоточка грузится')
    bot.send_photo(message.chat.id, nextRebus)
    msg = bot.send_message(message.chat.id, 'Введи правильный ответ по русски')

    bot.register_next_step_handler(msg, after_text_2, nextRebus)


bot.polling(none_stop=True, interval=0)