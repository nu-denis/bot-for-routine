from telebot import TeleBot, types
from config import config
from rivescript import RiveScript
import re

TOKEN = config.get('telegram', 'TOKEN')
MY_ID = config.get('telegram', 'MY_ID')
tg_bot = TeleBot(TOKEN, parse_mode=None)

dialog_bot = RiveScript(utf8=True)
dialog_bot.unicode_punctuation = re.compile(r'[.,!?;:]')
dialog_bot.load_directory('./scenarios')
dialog_bot.sort_replies()


def extract_custom_methods(text):
		return re.findall(r'<%([\w|_]*)=([\w|\s]*)%>', text)


def parse_custom_methods(custom_methods, markup) -> None:
		for name, value in custom_methods:
				if name == 'button':
						if markup is None:
								markup = types.ReplyKeyboardMarkup(row_width=2)
						button = types.KeyboardButton(value)
						markup.add(button)
				elif name == 'statistic_list':
						pass


@tg_bot.message_handler(content_types=['text'])
def get_text_messages(message):
		user_id = str(message.from_user.id)
		if user_id != MY_ID:
				tg_bot.send_message(user_id, "Sorry")

		text = message.text
		reply = dialog_bot.reply(user_id, text)
		custom_methods = extract_custom_methods(reply)

		markup = None
		parse_custom_methods(custom_methods, markup)
		tg_bot.send_message(user_id, reply, reply_markup=markup)


tg_bot.infinity_polling()
