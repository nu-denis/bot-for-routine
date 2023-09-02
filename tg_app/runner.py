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
        return last_message_id_by_chat_id[chat_id] < message_id
    return True


def is_working_time(date_time):
    if date_time.weekday() <= 4:
        if (9 == date_time.hour and 40 <= date_time.minute) or \
                10 <= date_time.hour < 19 or \
                (19 == date_time.hour and date_time.minute < 20):
            return True
    return False


@tg_bot.message_handler(commands=['help'])
def send_welcome(message):
    if check_last_updates(message):
        tg_bot.reply_to(message, 'Привет 👋\nЯ "Простой бот", умею следить за сообщениями в нерабочее время')


@tg_bot.message_handler(func=check_last_updates)
def echo_all(message):
    print('kek')
    if not is_working_time(datetime.now(timezoneSamara)):
        tg_bot.reply_to(message, TEXT_MESSAGE)


def run():
    tg_bot.infinity_polling()
