import telebot
import config
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot(config.token)
def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Hello", callback_data="1"))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(row_width=2)
    itembtn1 = KeyboardButton('asda 1')
    itembtn2 = KeyboardButton('☑')
    itembtn3 = KeyboardButton('◄')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Choose one letter:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def conversation(message):
    if message.text == "1":
        bot.send_message(message.chat.id, "Добре")
         if InlineKeyboardButton.callback_data == "Hello":
            bot.send_message(message.chat.id, "Helo-Helo!")

def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Hello", callback_data="Hello"))
    return markup
    if message.text == "Пісня 1":
        bot.send_message(message.chat.id, "Червона рута")
        if message.text == "Пісня 2":
            bot.send_message(message.chat.id, "Smells like teen spirit")
            if message.text == "Пісня 3":
            bot.send_message(message.chat.id, "Hot&Cold")
            else:
            bot.send_message(message.chat.id, "Тут інлайн кнопка", reply_markup=markup_inline())
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "Hello":
        print(call)
        bot.send_message(call.from_user.id, "Hello-hello")


bot.polling(none_stop=True)








