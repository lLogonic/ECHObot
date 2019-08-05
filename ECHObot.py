import telebot
#from telebot import apihelper

TOKEN = '756924458:AAEERMi3cF4X0SWR0pfejprNz4WeMCGQL3g'
#PROXY =


#apihelper.proxy = {'https': PROXY}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
	bot.polling(none_stop=True)