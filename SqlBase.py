import random

class DataBase:

    def CreateDataBase(db):
        db.cursor().execute("""CREATE TABLE IF NOT EXISTS game (
            login VARCHAR,
            path VARCHAR,
            gameType VARCHAR,
            correctAnswer VARCHAR,
            result INT
            )""")
        db.commit()


    def InsertNewUser(user, db):

        newUser = ''
        for value in db.cursor().execute("SELECT DISTINCT login FROM game where login = ?", [user]):
            newUser = str(value)[2:-3]

        if newUser == user:
                db.commit()
        else:
                values = [(user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/8csfnymbAwCTtos?x=1920&y=587&a=true&file=1%2520%25D0%25B4%25D0%25B8%25D1%2581%25D0%25BA%25D0%25BE%25D0%25B2%25D0%25BE%25D0%25B4.jpg&scalingup=0', 'rebus', 'дисковод', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/wPrkztSNGdxCcXD?x=1920&y=587&a=true&file=2%2520%25D0%25B1%25D0%25B0%25D0%25B3.jpg&scalingup=0', 'rebus', 'баг', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/KxDDf6wxWdngzfE?x=1920&y=587&a=true&file=3%2520%25D1%2584%25D0%25B8%25D0%25B4%25D0%25B1%25D0%25B5%25D0%25BA%2520.jpg&scalingup=0', 'rebus', 'фидбек', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/jqoX3fRxQB9xKWy?x=1920&y=587&a=true&file=4%2520%25D1%2584%25D1%2580%25D0%25BE%25D0%25BD%25D1%2582%25D0%25B5%25D0%25BD%25D0%25B4.jpg&scalingup=0', 'rebus', 'фронтенд', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/jq3pf9i9MoQEPp3?x=1920&y=587&a=true&file=5%2520%25D0%25B4%25D0%25B5%25D0%25B4%25D0%25BB%25D0%25B0%25D0%25B9%25D0%25BD.jpg&scalingup=0', 'rebus', 'дедлайн', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/D3SjKo3WeMqEKGK?x=1920&y=587&a=true&file=6%2520%25D1%2581%25D0%25BA%25D1%2580%25D0%25B8%25D0%25BF%25D1%2582%2520.jpg&scalingup=0', 'rebus', 'скрипт', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/KJHXmcSoqLPp3tC?x=1920&y=587&a=true&file=7%2520%25D1%2582%25D1%2580%25D0%25BE%25D1%258F%25D0%25BD.jpg&scalingup=0', 'rebus', 'троян', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/ptoLxAHjmkxxgjc?x=1920&y=587&a=true&file=8%2520%25D1%2581%25D0%25B5%25D0%25BD%25D1%258C%25D0%25BE%25D1%2580.jpg&scalingup=0', 'rebus', 'сеньор', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/n5gTMX6ZyxqLtwo?x=1920&y=587&a=true&file=9%2520%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B2%25D0%25BE%25D1%2580%25D0%25BA%25D0%25B8%25D0%25BD%25D0%25B3%2520.jpg&scalingup=0', 'rebus', 'нетворкинг', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/CsgnESAPtJZbfmM?x=1920&y=587&a=true&file=10%2520%25D0%25BA%25D0%25B5%25D0%25B9%25D1%2581.jpg&scalingup=0', 'rebus', 'кейс', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/YQBb2pkmzXM2doQ?x=1920&y=587&a=true&file=11%2520%25D0%25BC%25D0%25BE%25D0%25BD%25D0%25B8%25D1%2582%25D0%25BE%25D1%2580.jpg&scalingup=0', 'rebus', 'монитор', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/zS8Ha74jgn77Fns?x=1920&y=587&a=true&file=12%2520%25D1%2581%25D0%25BA%25D1%2580%25D0%25B0%25D0%25BC.jpg&scalingup=0', 'rebus', 'скрам', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/NJ57iRS4tFFCqsQ?x=1920&y=587&a=true&file=13%2520%25D0%25B3%25D0%25B8%25D1%2582.jpg&scalingup=0', 'rebus', 'гит', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/r2eSYP7FX3s36b9?x=1920&y=587&a=true&file=15%2520%25D1%2582%25D0%25B0%25D1%2581%25D0%25BA.jpg&scalingup=0', 'rebus', 'таск', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/f7R5sWCAWEmBxmA?x=1920&y=587&a=true&file=16%2520%25D1%2585%25D0%25BE%25D1%2582%25D1%2584%25D0%25B8%25D0%25BA%25D1%2581.jpg&scalingup=0', 'rebus', 'хотфикс', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/3CT7yAZLfAXfgJZ?x=1920&y=587&a=true&file=17%2520%25D0%25B4%25D0%25B5%25D0%25BF%25D0%25BB%25D0%25BE%25D0%25B9.jpg&scalingup=0', 'rebus', 'деплой', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/rTQLgWc44tnim5W?x=1920&y=587&a=true&file=18%2520%25D1%2580%25D0%25B5%25D0%25B2%25D1%258C%25D1%258E.jpg&scalingup=0', 'rebus', 'ревью', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/9iH6bcTnAYxZJ8N?x=1920&y=587&a=true&file=19%2520%25D0%25BF%25D1%2580%25D0%25BE%25D0%25B4.jpg&scalingup=0', 'rebus', 'прод', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/XXdHgpyGBKCocgw?x=1920&y=587&a=true&file=20%2520%25D0%25B4%25D0%25B6%25D0%25B0%25D0%25B2%25D0%25B0.jpg&scalingup=0', 'rebus', 'джава', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/eWqGbE2sxCxqAeg?x=1920&y=587&a=true&file=21%2520%25D1%258E%25D0%25B7%25D0%25B5%25D1%2580.jpg&scalingup=0', 'rebus', 'юзер', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/noZmPRAwdocMHik?x=1920&y=587&a=true&file=22%2520%25D1%2584%25D0%25B8%25D1%2587%25D0%25B0.jpg&scalingup=0', 'rebus', 'фича', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/gK36Cpt7XJZZfPZ?x=1920&y=587&a=true&file=23%2520%25D0%25BA%25D0%25BE%25D1%2581%25D1%2582%25D1%258B%25D0%25BB%25D1%258C.jpg&scalingup=0', 'rebus', 'костыль', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/pdsocP4K9KJ5ytX?x=1920&y=587&a=true&file=24%2520%25D0%25B4%25D0%25B5%25D0%25BC%25D0%25BA%25D0%25B0.jpg&scalingup=0', 'rebus', 'демка', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/moiE94QQ8BnAYrX?x=1920&y=587&a=true&file=25%2520%25D0%25BF%25D0%25B8%25D0%25BD%25D0%25B3.jpg&scalingup=0', 'rebus', 'пинг', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/sdJHXrM76AR4xPb?x=1920&y=587&a=true&file=26%2520%25D1%2580%25D0%25B5%25D0%25BB%25D0%25B8%25D0%25B7.jpg&scalingup=0', 'rebus', 'релиз', 0),
                    (user, 'https://disk.skbkontur.ru/index.php/apps/files_sharing/publicpreview/my5KKpf39A5TKQo?x=1920&y=587&a=true&file=27%2520%25D0%25BB%25D0%25B5%25D0%25B3%25D0%25B0%25D1%2581%25D0%25B8.jpg&scalingup=0', 'rebus', 'легаси', 0)]

                db.cursor().executemany("INSERT INTO game (login, path, gameType, correctAnswer, result) VALUES (?, ?, ?, ?, ?)", values)
                db.commit()






    def NextRebus(user, db):
        rebusList = []

        for value in db.cursor().execute("SELECT path FROM game where result = 0 and login = ?", [user]):
            rebusList.append(value)

        if rebusList != []:
            result = str(random.choice(rebusList))
            removeTwoFirstSymbols = result[2:]
            l = len(removeTwoFirstSymbols)
            return removeTwoFirstSymbols[:l - 3]
        else:
            return ''




    def SelectCorrectAnswer(db, path):

        trueAnswer = []

        for value in db.cursor().execute("SELECT DISTINCT correctAnswer FROM game where path = ?", [path]):
            trueAnswer.append(value)

        return str(trueAnswer)[3:-4]


    def AddPoints (db, user, path):
        db.cursor().execute("Update game SET result = 1 where login = ? and path = ?", [user, path])
        db.commit()

    def SelectFromDataBase(db):
        for value in db.cursor().execute("SELECT * FROM game"):
            print(value)


    def DropDataBase(db):
        db.cursor().execute("DROP TABLE game")

    def SelectLeaderBoard(db):
        leaderBoard = []

        for value in db.cursor().execute("SELECT login, SUM (result) FROM game group by login order by SUM(result) desc"):
            leaderBoard.append(value)
        return leaderBoard