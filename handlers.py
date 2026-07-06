from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.massage.reply_text("Salom! Movie botga xush kelibsiz 🎥")