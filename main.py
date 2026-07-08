import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, Updater

from movie_list import movies as movie_list 
from movie_list import random_movies

updater = Updater("8991276893:AAHF6ZV3ZgSHM8IgBVs_fPRNdabfoAMUNPs", use_context=True)
dp = updater.dispatcher


def movie_menu():
    keyboard = [
        [
            InlineKeyboardButton("🎥 Action", callback_data="action"),
            InlineKeyboardButton("😂 Comedy", callback_data="comedy"),
        ],
        [
            InlineKeyboardButton("🎭 Drama", callback_data="drama"),
            InlineKeyboardButton("😱 Horror", callback_data="horror"),
        ],
        [
            InlineKeyboardButton("🤔 RANDOM", callback_data="random")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def main_menu():
    keyboard = [[KeyboardButton("/movie")]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Salom! Movie botga xush kelibsiz 🎥", reply_markup=main_menu()
    )


def movies(update: Update, context: CallbackContext):

    update.message.reply_text(
        "🎥 Kategoriya tanlang:", reply_markup=movie_menu()
    )



def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    category = query.data

    if category in movie_list:
        film = random.choice(movie_list[category])
        text = f"🎥 Tavsiya:\n{film['name']}"
        image_url = film["image"]

        query.message.delete()
        context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=image_url,
            caption=text,
            reply_markup=movie_menu(),  
        )
        
    elif category == "random":
            film = random.choice(random_movies) 
            
            text = f"🎲 Tasodifiy kino:\n{film['title']} ({film['year']})"
            
            image_url = film["poster"]

            query.message.delete()
            context.bot.send_photo(
                chat_id=query.message.chat_id,
                photo=image_url,
                caption=text,
                reply_markup=movie_menu(),  
            )
    else:
         print("❌ Nomalum kategoriya")
            



dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("movie", movies))

dp.add_handler(CallbackQueryHandler(button_handler))


updater.start_polling()
updater.idle()