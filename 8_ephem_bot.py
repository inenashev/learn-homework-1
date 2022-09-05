"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

def is_valid_name(name):
    allowed_input = []
    for e in ephem._libastro.builtin_planets()[:8]:
        allowed_input.append(e[2])
    return name in allowed_input

def check_input(name):
    split = name.split(" ")
    if len(split) == 2:
        return split[1]
    else:
        return None

def planet(update, context):
    text = update.message.text
    checked_text = check_input(text)
    if checked_text:
        planet_name = checked_text
        if is_valid_name(planet_name):
            pl = getattr(ephem, planet_name)(ephem.now())
            pl.compute()
            constellation = str(ephem.constellation(pl))
            update.message.reply_text(constellation)
        else:
            update.message.reply_text("Не нашел имя планеты ввод в формате /planet Mars")
    else:
        update.message.reply_text("Не распознал имя планеты, попробуйте еще раз")


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
