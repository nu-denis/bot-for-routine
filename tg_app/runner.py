from config import config
from datetime import datetime
import pytz
from telebot import TeleBot
from .utils import get_last_message_id_by_chat_id

TOKEN = config.get('telegram', 'TOKEN')
tg_bot = TeleBot(TOKEN, parse_mode=None)
last_message_id_by_chat_id = get_last_message_id_by_chat_id(tg_bot.get_updates())
timezoneSamara = pytz.timezone("Europe/Samara")
TEXT_MESSAGE = '''Команда Happy Panda работает:\n\nс пн-пт 9:00-18:00 мск.\n\n Будем рады ответить вам в рабочее время 🐼'''


def check_last_updates(msg):
    message_id = msg.id
    chat_id = msg.chat.id
    print('info', chat_id, message_id)
    if chat_id in last_message_id_by_chat_id:
        return last_message_id_by_chat_id[chat_id] <= message_id
    return True


def is_working_time():
    now = datetime.now(timezoneSamara)
    if now.weekday() <= 4:
        if 10 < now.hour < 19:
            return True
    return False


@tg_bot.message_handler(func=check_last_updates)
def echo_all(message):
    print('kek')
    if not is_working_time():
        tg_bot.reply_to(message, TEXT_MESSAGE)


def run():
    tg_bot.infinity_polling()
