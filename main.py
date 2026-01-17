import os
import json
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# ===== Google Sheets =====
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, SCOPE)
client = gspread.authorize(creds)

SHEET_NAME = "Семейный бюджет"
sheet = client.open(SHEET_NAME).worksheet("Operations")

# ===== Telegram handler =====
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.message.from_user.first_name
    user_id = update.message.from_user.id
    date = datetime.now().strftime("%d.%m.%Y")

    row = [
        date,      # Date
        user,      # User
        user_id,   # User_ID
        "Expense", # Type (пока фикс)
        "",        # Category
        "",        # Amount
        "",        # Budget
        "",        # Goal
        text       # Comment
    ]

    sheet.append_row(row)
    await update.message.reply_text("Записала 👍")

# ===== Start bot =====
app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
