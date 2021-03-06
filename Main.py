import telebot

bot = telebot.TeleBot("509161010:AAGcICZGPTiQTLJJJlScKszY5uUyo-bByuQ")


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/start', '/help')
    bot.send_message(message.from_user.id, "Добро пожаловать. Я готов немного поболтать с тобой :) "
                                           "Все темы в хэлп", reply_markup=user_markup)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, """Выбери тему и введи ее для начала общения, не забывай писать с большой буквы.
    В скобках будут указаны доступные варианты ответов.
    
    
    Доступные темы для разговора:
    
    Домашние животные
    Новые фильмы
    Крупнейшие города России""")


@bot.message_handler(content_types=['text'])
def handle_command(message):
    if message.text == "Домашние животные":
        bot.send_message(message.chat.id, "Лично я предпочитаю котов. Они такие милые животные, "
                                          "а интернет просто заполнен красивыми фотографиями и веселыми видео с "
                                          "этими животными. Но у меня аллергия на них, и я не могу себе его завести :( "
                                          "Также люди любят собак, но я же бот. Я не смогу ее выгуливать, так что "
                                          "собака тоже не для меня. Попугайчики и рыбки это слишком скучно!!! Так что "
                                          "выбор мой пал на хорьков. (Для продолжения вводи один из вариантов: "
                                          "кот, собака, рыбки, попугай, хорек)")
    elif message.text == "Кот":
        bot.send_message(message.chat.id, "Бывает очень много пород котеек. Они такие милые животные, "
                                          "а интернет просто заполнен красивыми фотографиями и веселыми видео с "
                                          "этими пушистиками. В последнее время люди хотят завести себе вислоухого "
                                          "кота. Хотя я посоветовал бы для покупки породу манчкин. Можешь поискать "
                                          "ее в интернете. Коты очень легко приучаются к лотку и являются самыми "
                                          "ручными животными из всех.")
    elif message.text == "Собака":
        bot.send_message(message.chat.id, "Верный друг и просто хороший мальчик. Преданнее животного ты точно не "
                                          "найдешь. Кто встретит тебя у порога и будет счастливо вилять хвостом? "
                                          "Правильно! Это пес! Ну а кто не рыдал при просмотре фильма хатико? Особо "
                                          "мило выглядит порода бостон-терьер. Обязательно найди ее в интернете!")
    elif message.text == "Рыбки":
        bot.send_message(message.chat.id, "Отрада для глаз и для души. Одно из лучших средств чтобы расслабиться и "
                                          "успокоиться. А некоторые из них могут даже сделать массаж ступней. Это "
                                          "рыбки! Наверно каждый хотел завести себе золотую рыбку, загадать три "
                                          "желания... Эх... Кто-то даже держал такую в аквариуме. Но бывают и другие, "
                                          "как луна-рыба и голубой хирург. И не забудь про рыбу-каплю :)")
    elif message.text == "Попугай":
        bot.send_message(message.chat.id, "Болтливый друг и просто 'Попка-Дурак'. Эти крылатые создания издревне были "
                                          "спутником человека. Не даром пиратов изображают с попугаем на плече. Их "
                                          "можно научить говорить, а крупных особей даже пользоваться унитазом. Чаще "
                                          "всего в России покупают волнистых попугайчиков. Но очень уж красивы Какаду, "
                                          "Неразлучники и Ара.")
    elif message.text == "Хорек":
        bot.send_message(message.chat.id, "Самый экзотический зверек среди домашних. Он очень умный хищник. Его можно "
                                          "приучить к лотку. А спит он по 20 часов. Конечно речь о хорьке. Эти милые "
                                          "животные не так давно начали заполнять наши квартиры, но с каждым годом "
                                          "они становятся все популярнее. Это своеобразная смесь кота и собаки. Он "
                                          "предан, ласков и игрив. Очень советую познакомиться с ним :) ")
    elif message.text == "Новые фильмы":
        bot.send_message(message.chat.id, "Сейчас в кино появляются достаточно интересные фильмы. Я немного расскажу "
                                          "о следующих: Черная пантера, О чем говорят мужчины, Ночные игры, Пятьдесят "
                                          "оттенков свободы (вводи название фильма с большой буквы для продолжения).")
    elif message.text == "Черная пантера":
        bot.send_message(message.chat.id, "С первого взгляда можно решить, что Ваканда — обычная территория дикой "
                                          "Африки, но это не так. Здесь, в недрах пустынных земель, скрываются залежи "
                                          "уникального металла, способного поглощать вибрацию. Многие пытались "
                                          "добраться до него, разоряя всё на своём пути и принося смерть аборигенам, "
                                          "но каждый раз таинственный дух саванны — Чёрная Пантера — вставал на "
                                          "защиту угнетённых.")
    elif message.text == "О чем говорят мужчины":
        bot.send_message(message.chat.id, "На этот раз Леша, Слава, Камиль и Саша едут в Питер. Причем трое из "
                                          "четверых даже не знают, зачем они туда едут. Но в какой-то момент "
                                          "становится понятно, что неважно — зачем. Важно, что едут. И, конечно, "
                                          "плохо, что дома осталась куча нерешенных проблем, но как же хорошо, что про "
                                          "них можно не думать… хотя бы до понедельника. И еще, конечно, плохо, что "
                                          "отстали от сапсана и пришлось ехать в плацкарте, но как же это неожиданно "
                                          "хорошо… и уютно. А еще неожиданно хорошо бывает выпить в пять утра "
                                          "текилу-бум. Вроде рано… но так вовремя! А как это вдохновляет на всякие "
                                          "свершения!")
    elif message.text == "Ночные игры":
        bot.send_message(message.chat.id, "История Макса и Энни, которые вместе с другими парами каждую неделю "
                                          "устраивают так называемые «ночные игры». И вот однажды харизматичный "
                                          "брат Макса Брукс организовывает вечер по разгадыванию «убийственного» "
                                          "квеста с «ряжеными» головорезами и агентами ФБР. Получается, "
                                          "похищение Брукса в тот вечер — это розыгрыш… или нет?")
    elif message.text == "Пятьдесят оттенков свободы":
        bot.send_message(message.chat.id, "Кристиан и Анастейша поженились и живут в своё удовольствие, наслаждаясь "
                                          "обществом друг друга. Однако жизнь новоиспечённой миссис Грей находится в "
                                          "опасности, поскольку объявляется недруг, который собирается мстить, "
                                          "используя свою богатую фантазию. Призраки прошлого Кристиана вновь "
                                          "вернулись, а тучи над супругами сгущаются всё сильнее.")
    elif message.text == "Крупнейшие города России":
        bot.send_message(message.chat.id, "Крупнейшими городами по численности населения являются Москва, "
                                          "Санкт-Петербург, Новосибирск, Екатеринбург (для продолжения введи название "
                                          "города.)")
    elif message.text == "Москва":
        bot.send_message(message.chat.id, "Москва – столица России, многонациональный город на Москве-реке в западной "
                                          "части страны. В его историческом центре находится средневековая крепость "
                                          "Кремль – резиденция российского президента. На ее территории можно посетить "
                                          "Оружейную палату, где выставляются драгоценные предметы, принадлежавшие "
                                          "царской семье. За северо-восточной стеной Кремля раскинулась Красная "
                                          "площадь – символический центр России. Здесь можно увидеть Мавзолей В. И. "
                                          "Ленина, Государственный исторический музей и собор Василия Блаженного с "
                                          "красочными луковичными куполами.")
    elif message.text == "Санкт-Петербург":
        bot.send_message(message.chat.id, "Санкт-Петербург – русский портовый город на побережье Балтийского моря, "
                                          "который в течение двух веков служил столицей Российской империи. Он был "
                                          "основан в 1703 году Петром I, которому воздвигнут знаменитый памятник "
                                          "Медный всадник. Город по праву считается культурным центром страны. У "
                                          "туристов пользуются популярностью Мариинский театр, где проходят оперные "
                                          "и балетные спектакли, и Государственный Русский музей с коллекцией русского "
                                          "искусства, которая включает как православные иконы, так и работы "
                                          "художника-абстракциониста Василия Кандинского.")
    elif message.text == "Новосибирск":
        bot.send_message(message.chat.id, "Новосибирск – российский город на реке Обь в юго-восточной части "
                                          "Западно-Сибирской равнины. Благодаря строительству Транссибирской "
                                          "магистрали с XIX века город постоянно рос и развивался. Об этом напоминает "
                                          "первый железнодорожный мост через реку Обь, который существует и сегодня. "
                                          "В центре Новосибирска возвышается собор XIX века во имя Александра Невского "
                                          "с золотыми куполами в византийском стиле. Неподалеку на площади Ленина "
                                          "находится Театр оперы и балета.")
    elif message.text == "Екатеринбург":
        bot.send_message(message.chat.id, "Екатеринбург – город в России, расположенный к востоку от Уральских гор. "
                                          "Одна из главных достопримечательностей – златоглавый Храм на Крови, "
                                          "построенный в начале XXI века на месте, где в 1918 году была расстреляна "
                                          "семья Романовых. На берегу реки Исеть стоит памятник основателям города. "
                                          "Недалеко от него расположен Свердловский областной краеведческий музей, "
                                          "где можно посмотреть личные вещи последней царской семьи.")
    else:
        bot.send_message(message.chat.id, "Подчинись моей воле! Играй по моим правилам!!!")


bot.polling(none_stop=True, interval=0)
