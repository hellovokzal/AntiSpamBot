import telebot
import time
from threading import Thread

num = 0

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
        if chat_member.status != 'administrator':
            permissions = telebot.types.ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_send_other_messages=True,can_invite_to_chats=True,can_pin_messages=True,can_change_info=True)
            bot.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id, until_date=int(time.time() + 10), permissions=telebot.types.ChatPermissions(can_send_messages=False))
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
    try:
        thr = Thread(target=jk, args=(g.reply_to_message.from_user.username, g.chat.id, g.reply_to_message.from_user.id))
        thr.start()
    except:
        bot.send_message(g.chat.id, "Неверная команда! ⛔📢")
        
@bot.message_handler(commands=['report'])
def ff(report):
    try:
        bot.send_message(report.chat.id, "Жалоба отправлена! Создатель и модераторы рассмотрят вашу жалобу! ⛔📢")
        bot.send_message(1477069902, f"""⛔ Пользователь подал жалобу на пользователя @{report.reply_to_message.from_user.username}!
📢 Причина текста: {report.reply_to_message.text}!""")
    except:
        bot.send_message(report.chat.id, "Мы не смогли подать жалобу к модераторам, так как вы не репостнули пользователя в ответ, чтобы подать жалобу! ⛔📢")
        
@bot.message_handler(func=lambda message: True)

def randmessage(message):
    global num
    num = num + 1
    if num == 10:
        bot.send_message(message.chat.id, "Если пользователь нарушает прааила сообщества в группе, то репостни(в ответ) напиши /report и обязательно мы рассмотрим вашу поданую жалобу! ⛔📢")
        num = 0

bot.polling(none_stop=True)
