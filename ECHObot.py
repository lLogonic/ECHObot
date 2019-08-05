import telebot
from telebot.types import Message
#from telebot import apihelper

TOKEN = '756924458:AAEERMi3cF4X0SWR0pfejprNz4WeMCGQL3g'
#PROXY =


#apihelper.proxy = {'https': PROXY}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types = ["text"])
def mess(message: Message):
	bot.reply_to(message, message.text.upper())


	bot.polling(none_stop = True)