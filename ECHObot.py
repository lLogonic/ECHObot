import telebot
#from telebot import apihelper

TOKEN = '756924458:AAEERMi3cF4X0SWR0pfejprNz4WeMCGQL3g'
#PROXY =


#apihelper.proxy = {'https': PROXY}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['/start'])
def handle_start(message):
	pass

@bot.message_handler(content_types = ["text"])
def mess(message):
	bot.send.message(message.chat.id, message.text)

if __name__ == '__main__':
	bot.polling(none_stop = True)