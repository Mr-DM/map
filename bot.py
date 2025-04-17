import telebot
from config import *
from logic import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может показывать города на карте. Напиши /help для списка команд.")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, """
    🤖 *Доступные команды бота*:

    /start — Начать общение с ботом. Вы получите приветственное сообщение.

    /help — Показать это справочное сообщение.

    /show_city <цвет> <город> — Показать указанный город на карте.
    Пример: `/show_city blue Tokyo`
    Если цвет не указан Код не сработает.

    /remember_city <город> — Сохранить город в ваш список посещённых.
    Пример: `/remember_city London`

    /show_my_cities — Показать все ваши сохранённые города на карте.

    📍 Убедитесь, что названия городов пишутся на *английском языке*.
    """)

@bot.message_handler(commands=['show_city'])
def handle_show_city(message):
    city_name = message.text.split()[-1]
    color = message.text.split()[1] 
    
    # Реализуй отрисовку города по запросу
    
    manager.draw_distance(city_name, color)
    bot.send_photo(message.chat.id, open('map.png', 'rb'))


@bot.message_handler(commands=['remember_city'])
def handle_remember_city(message):
    user_id = message.chat.id
    city_name = message.text.split()[-1]
    if manager.add_city(user_id, city_name):
        bot.send_message(message.chat.id, f'Город {city_name} успешно сохранен!')
    else:
        bot.send_message(message.chat.id, 'Такого города я не знаю. Убедись, что он написан на английском!')

@bot.message_handler(commands=['show_my_cities'])
def handle_show_visited_cities(message):
    cities = manager.select_cities(message.chat.id)
    # Реализуй отрисовку всех городов



if __name__=="__main__":
    manager = DB_Map(DATABASE)
    bot.polling()
