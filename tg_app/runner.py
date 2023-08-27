from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import config

TOKEN = config.get('telegram', 'TOKEN')
tg_app = ApplicationBuilder().token(TOKEN).build()


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


def run():
    tg_app.add_handler(CommandHandler("hello", hello))
    tg_app.run_polling()
