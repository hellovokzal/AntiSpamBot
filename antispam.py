import telebot
import time
import time

bot = telebot.TeleBot("7334734746:AAE_xWuTtPZOwt1VZCFUsH7L4FYu-zAc3BY")

@bot.message_handler(commands=['m'])

def h(m):
    bot.delete_message(m.chat.id, m.message_id)
    bot.restrict_chat_member(m.chat.id, m.from_user.id, until_date=600)
    
bot.polling(none_stop=True)
