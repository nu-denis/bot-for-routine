import telebot
from config import config

TOKEN = config.get('telegram', 'TOKEN')
MY_ID = config.get('telegram', 'MY_ID')
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
		user_id = str(message.from_user.id)
		if user_id == MY_ID:
				bot.send_message(user_id, "Ok")
		else:
				bot.send_message(user_id, "Sorry")


bot.infinity_polling()
