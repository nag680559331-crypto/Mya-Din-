import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

PRESET_ACTIONS = {
    "စည်းမျဉ်း": "Group စည်းမျဉ်းများ:\n1. Spam စာများ မပို့ရ။\n2. လေးစားမှုရှိစွာ ပြောဆိုရန်။",
    "ဝန်ဆောင်မှု": "ရရှိနိုင်သော ဝန်ဆောင်မှုများ:\n• Auto Reply System\n• Custom Keyword Triggers",
    "အကူအညီ": "သိလိုသော စကားလုံးကို ရိုက်ထည့်ပါ (ဥပမာ - စည်းမျဉ်း၊ ဝန်ဆောင်မှု)။"
}

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [["စည်းမျဉ်း", "ဝန်ဆောင်မှု"], ["အကူအညီ"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "မင်္ဂလာပါ! သတ်မှတ်ထားသော လုပ်ဆောင်ချက်များအတိုင်း အလိုအလျောက် တုံ့ပြန်ပေးမည့် Bot ဖြစ်ပါသည်။",
        reply_markup=MAIN_KEYBOARD
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.strip()
    if text in PRESET_ACTIONS:
        await update.message.reply_text(PRESET_ACTIONS[text], reply_markup=MAIN_KEYBOARD)

def main():
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN မတွေ့ပါ!")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("Telegram Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
