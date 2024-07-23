import telebot
import time

# Замените этот токен на токен вашего бота
BOT_TOKEN = "7334734746:AAE_xWuTtPZOwt1VZCFUsH7L4FYu-zAc3BY"

# Создайте бота
bot = telebot.TeleBot(BOT_TOKEN)

# Словарь для отслеживания сообщений пользователей
user_messages = {}

# Время для проверки сообщений
check_interval = 1

# Минимальное количество сообщений для мута
mute_threshold = 3

# Время мута (в секундах)
mute_duration = 600

@bot.message_handler(func=lambda message: True)
def handle_message(message):
  global user_messages
  # Получите имя пользователя и ID
  user_id = message.from_user.id
  username = message.from_user.username

  # Обновите словарь сообщений
  if user_id in user_messages:
    user_messages[user_id].append(time.time())
  else:
    user_messages[user_id] = [time.time()]

  # Проверьте, превышает ли количество сообщений порог
  if len(user_messages[user_id]) >= mute_threshold:
    # Получите время последнего сообщения
    last_message_time = user_messages[user_id][-1]

    # Проверьте, прошло ли достаточно времени
    if time.time() - last_message_time < check_interval:
      # Отправьте сообщение о муте
      bot.send_message(message.chat.id, f"Пользователь @{username} заблокирован за спам на 10 минут! ⛔📢")
      user_messages = {}

      # Замутьте пользователя
      bot.restrict_chat_member(message.chat.id, user_id, until_date=int(time.time() + mute_duration), can_send_messages=False)

      # Очистите список сообщений пользователя
      user_messages[user_id] = []

# Запустите бота
bot.polling(none_stop=True)
