import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 1. Берём токен из переменных окружения Render
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 2. Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет 👋\n"
        "Я бот для ведения бюджета.\n\n"
        "Пока я умею:\n"
        "— отвечать на /start\n\n"
        "Скоро добавим расходы, доходы и отчёты 💰"
    )

# 3. Запуск бота
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

# 4. Точка входа
if name == "__main__":
    main()
