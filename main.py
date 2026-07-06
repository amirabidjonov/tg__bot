from telegram.ext import Updater, CommandHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup

updater = Updater("8991276893:AAHF6ZV3ZgSHM8IgBVs_fPRNdabfoAMUNPs", use_context=True)

dp = updater.dispatcher

def start(update, context):
    update.message.reply_text("Salom! Movie botga xush kelibsiz 🎥")

def movies(update, context):
    update.message.replay_text("1.Inception (Muqaddima), 2.The Dark Knight (Qora ritsar), 3.Interstellar (Yulduzlararo), 4.The Shawshank Redemption (Shoushenkdan qochish), 5.The Matrix (Matritsa), 6.Gladiator (Gladiator), 7.The Lord of the Rings (Uzuklar hukmdori), 8.Forrest Gump (Forrest Gamp), 9.Shutter Island (Laʼnatlanganlar oroli), 10.The Green Mile (Yashil milya)")


def main_menu():
    keyboard = [
        [KeyboardButton("/movies")],[KeyboardButton("/sketch")]
    ]


dp.add_handler(CommandHandler("start", start))

dp.add_handler(CommandHandler("movies", movies))


updater.start_polling()

updater.idle()
