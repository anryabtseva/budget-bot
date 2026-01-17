import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет 👋\nЯ бот для учёта бюджета 💰"
    )

def main():
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN не найден в переменных окружения")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()
