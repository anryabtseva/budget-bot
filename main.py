import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# Берем токен из переменных окружения Render
BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет 👋 Я бот для учета бюджета.\n"
        "Напиши сумму, и я ее сохраню."
    )

def main():
    if not BOT_TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN в Environment Variables")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()
