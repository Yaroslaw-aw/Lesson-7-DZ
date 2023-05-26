# Задача 3. Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
import requests

myFirstBot = telebot.TeleBot("6154888943:AAHkZBEyCJKP_KgzDyvB7PBIJoFgfKHXCJk")

bots_numbres: dict = {}
players_attempts: dict = {}

@myFirstBot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    myFirstBot.reply_to(message, 
                        "Привет, я умею показывать погоду, котиков и играть в игру 'угадай число'." +
                        "\nЧтобы узнать погоду, напишите слово погода." +
                        "\nЧтобы посмотреть котика, напишите слово котик." +
                        "\nЧтобы сыграть в игру, напишите слово игра." +
                        "\nПриятного время препровождения ;)"
                        )


@myFirstBot.message_handler(content_types=['text'])
def greetings(message):

    global x, count
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    text: str = message.text.lower()

    if 'привет' in text:
        myFirstBot.reply_to(message, f'Привет, {user_name}!')

    elif 'погода' in text:
        req = requests.get('https://wttr.in/?0T')
        myFirstBot.reply_to(message, req.text)

    elif 'котик' in text:
        req = requests.get('https://cataas.com/cat')
        myFirstBot.send_photo(user_id, req.content)

    elif 'игра' in text:
        import random
        bots_numbres[user_id] = random.randint(1, 1000)
        players_attempts[user_id] = 0
        myFirstBot.reply_to(message, f'Я загадал случайное число от 1 до 1000.\n' + 
                            "Угадайте, какое?")

    else:
        if text.isdigit():

            attempt = int(message.text)

            if attempt == bots_numbres[user_id]:
                players_attempts[user_id] += 1
                myFirstBot.reply_to(message, f'Поздравляю, вы угадали!\nC {players_attempts[user_id]} попытки!')
                del players_attempts[user_id]
                del bots_numbres[user_id]
                print(players_attempts)

            elif attempt > bots_numbres[user_id]:
                players_attempts[user_id] += 1
                myFirstBot.reply_to(message, f'Загаданное число меньше')
                return players_attempts[user_id]

            elif attempt < bots_numbres[user_id]:
                players_attempts[user_id] += 1
                myFirstBot.reply_to(message, f'Загаданное число больше')
                return players_attempts[user_id]

        else:
            myFirstBot.reply_to(message, f'Вы ввели неверное число или неизвестную мне команду, попробуйте ещё раз.')

myFirstBot.polling()