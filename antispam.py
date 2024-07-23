import telebot
import time

bot = telebot.TeleBot("7334734746:AAE_xWuTtPZOwt1VZCFUsH7L4FYu-zAc3BY")

# Словарь для хранения информации о пользователях и их спам-активности
users = {}

# Функция для обработки сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Получаем ID пользователя
    user_id = message.from_user.id

    # Проверяем, есть ли информация о пользователе в словаре
    if user_id not in users:
        # Если нет, инициализируем его запись
        users[user_id] = {
            "last_message_time": 0,
            "message_count": 0
        }

    # Получаем время последнего сообщения
    last_message_time = users[user_id]["last_message_time"]

    # Проверяем, прошло ли больше 1 секунды с момента последнего сообщения
    if time.time() - last_message_time > 1:
        # Сбрасываем счетчик сообщений
        users[user_id]["message_count"] = 0
    else:
        # Увеличиваем счетчик сообщений
        users[user_id]["message_count"] += 1

    # Проверяем, достигло ли количество сообщений 3
    if users[user_id]["message_count"] >= 3:
        # Мут пользователя на 600 секунд
        bot.restrict_chat_member(message.chat.id, user_id, until_date=int(time.time()) + 600)
        bot.send_message(message.chat.id, f"Пользователь @{message.from_user.username} замучен на 10 минут за спам!")
        # Обновляем время последнего сообщения
        users[user_id]["last_message_time"] = time.time()

    # Обновляем время последнего сообщения
    users[user_id]["last_message_time"] = time.time()

# Запускаем бота
bot.polling(none_stop=True)
