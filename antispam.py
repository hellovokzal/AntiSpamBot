import telebot
import time
from threading import Thread

bot = telebot.TeleBot("7334734746:AAE_xWuTtPZOwt1VZCFUsH7L4FYu-zAc3BY")

def g(usr, id, id_user):
    time.sleep(600)
    bot.send_message(id, f"@{usr}, следите за правилами чата и не нарушайте или могут в большой срок дать мут на 2 раза больше! 📢")
    permissions = telebot.types.ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_send_other_messages=True,can_invite_to_chats=True,can_pin_messages=True,can_change_info=True)

    bot.restrict_chat_member(id, id_user, permissions=permissions)
    
def jk(usr, id, id_user):
    bot.send_message(id, f"@{usr}, следите за правилами чата и не нарушайте или могут в большой срок дать мут на 2 раза больше! 📢")
    permissions = telebot.types.ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_send_other_messages=True,can_invite_to_chats=True,can_pin_messages=True,can_change_info=True)
    bot.restrict_chat_member(id, id_user, permissions=permissions)

@bot.message_handler(commands=['m'])
def h(m):
    global until_date
    bot.delete_message(m.chat.id, m.message_id)
    
    # Проверка, является ли пользователь администратором
    try:
        chat_member = bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        if chat_member.status == 'administrator':
            permissions = telebot.types.ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_send_other_messages=True,can_invite_to_chats=True,can_pin_messages=True,can_change_info=True)
            bot.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id, permissions=permissions)
            bot.send_message(m.chat.id, f"@{m.reply_to_message.from_user.username} заблокирован на 10 минут за нарушение правил. Будьте осторожны с правилами и следите за правилами! ⛔📢")
            thr = Thread(target=g, args=(m.reply_to_message.from_user.username, m.chat.id, m.reply_to_message.from_user.id))
            thr.start()
        else:
            bot.send_message(m.chat.id, "Невозможно ограничить права администратора.")
    except:
        bot.send_message(m.chat.id, "Команды неверны! ⛔📢")
        
@bot.message_handler(commands=['u'])

def j(g):
    bot.delete_message(g.chat.id, g.message_id)
    thr = Thread(target=jk, args=(g.reply_to_message.from_user.username, g.chat.id, g.reply_to_message.from_user.id))
    thr.start()

bot.polling(none_stop=True)
