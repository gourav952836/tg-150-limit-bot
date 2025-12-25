import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")
MAX_CHARS = 150

async def limit_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        if len(update.message.text) > MAX_CHARS:
            await update.message.delete()
            await update.message.reply_text("❌ 150 अक्षर से ज्यादा मैसेज allowed नहीं है")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, limit_message))
app.run_polling()
