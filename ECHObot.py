import telebot
from telebot.types import Message
#from telebot import apihelper

TOKEN = '756924458:AAEERMi3cF4X0SWR0pfejprNz4WeMCGQL3g'
#PROXY =


#apihelper.proxy = {'https': PROXY}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет')

@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, message.text.upper())

bot.polling()