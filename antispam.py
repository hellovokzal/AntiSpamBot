import telebot
from datetime import datetime, timedelta

# Замените "7334734746:AAE_xWuTtPZOwt1VZCFUsH7L4FYu-zAc3BY" на ваш токен
bot = telebot.TeleBot("7334734746:AAE_xWuTtPZOwt1VZCFUsH7L4FYu-zAc3BY")

# Словарь для хранения спама пользователей
spam_users = {}

# Время мута в секундах
mute_duration = 600

# Предел спама
spam_limit = 3

# Время в секундах между сообщениями
spam_interval = 1

# Стикер для предупреждения о спаме
spam_sticker = "CAACAgIAAxkBAAEG9GFi50uN2hX5W-pQ56zR75oZ8t8gAAI1QADw7W_R24c205hJ6oLgQ"  # Замените на ваш ID стикера

# Стикер для уведомления о mute
mute_sticker = "CAACAgIAAxkBAAEG9GFj2D7L4Lh2Z8qI2-F1wJ65m00AAI2QADw7W_R-G4z_T85w7LAQ"  # Замените на ваш ID стикера

@bot.message_handler(content_types=['text'])
def handle_message(message):
    user_id = message.from_user.id

    # Проверяем, есть ли пользователь в словаре спама
    if user_id not in spam_users:
        spam_users[user_id] = {"count": 0, "last_message_time": datetime.now()}
    else:
        # Получаем время последнего сообщения
        last_message_time = spam_users[user_id]["last_message_time"]

        # Проверяем, прошло ли время с последнего сообщения
        if (datetime.now() - last_message_time).total_seconds() < spam_interval:
            # Увеличиваем счётчик спама
            spam_users[user_id]["count"] += 1
            spam_users[user_id]["last_message_time"] = datetime.now()

            # Проверяем, достиг ли пользователь предела спама
            if spam_users[user_id]["count"] >= spam_limit:
                # Мутим пользователя
                bot.restrict_chat_member(
                    message.chat.id,
                    user_id,
                    until_date=datetime.now() + timedelta(seconds=mute_duration),
                    can_send_messages=False
                )
                # Отправляем стикер о mute
                bot.send_sticker(message.chat.id, mute_sticker)
                # Сбрасываем счётчик спама
                spam_users[user_id]["count"] = 0
        else:
            # Обновляем время последнего сообщения
            spam_users[user_id]["last_message_time"] = datetime.now()

            # Проверяем, достиг ли пользователь предела спама
            if spam_users[user_id]["count"] >= spam_limit:
                # Отправляем стикер о предупреждении
                bot.send_sticker(message.chat.id, spam_sticker)

bot.polling(none_stop=True)
