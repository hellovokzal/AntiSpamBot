import telebot
import time
from threading import Thread

bot = telebot.TeleBot("7334734746:AAE_xWuTtPZOwt1VZCFUsH7L4FYu-zAc3BY")

def g(usr, id):
    time.sleep(600)
    bot.send_message(id, f"@{usr}, следите за правилами чата и не нарушайте или могут в большой срок дать мут на 2 раза больше! 📢")

@bot.message_handler(commands=['m'])
def h(m):
    global until_date
    bot.delete_message(m.chat.id, m.message_id)
    
    # Проверка, является ли пользователь администратором
    chat_member = bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id)
    if chat_member.status != 'administrator':
        bot.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id, until_date=int(time.time() + 600), permissions=telebot.types.ChatPermissions(can_send_messages=False))
        bot.send_message(m.chat.id, f"@{m.reply_to_message.from_user.username} заблокирован на 10 минут за нарушение правил. Будьте осторожны с правилами и следите за правилами! ⛔📢")
        thr = Thread(target=g, args=(m.reply_to_message.from_user.username, m.chat.id))
        thr.start()
    else:
        bot.send_message(m.chat.id, "Невозможно ограничить права администратора.")

bot.polling(none_stop=True)
