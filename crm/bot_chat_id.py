from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

API_TOKEN = '7110448157:AAHlcqtKD1bLeNX1p2QtZgxs7u3hTMGD9VE'


async def get_updates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда для получения последнего обновления"""
    await update.message.reply_text(str(update))


def main():
    # Создаем приложение с использованием токена
    application = ApplicationBuilder().token(API_TOKEN).build()

    # Добавляем обработчик команды /getUpdates
    application.add_handler(CommandHandler('getUpdates', get_updates))

    # Запускаем бота
    application.run_polling()


if __name__ == "__main__":
    main()
