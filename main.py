import telebot
from player import Player
from spaceship import Spaceship
from database_manager import Database_Manager

bot = telebot.TeleBot('7192017546:AAHmm8rgHh2sR_wHTYMh0pqS_5NWUPJRPGc', skip_pending=True)

@bot.message_handler()
def answer(message):
	if message.text == "Привет":
		db = Database_Manager()
		bot.reply_to(message, db.add_user(message.from_user.id, message.from_user.first_name))

bot.infinity_polling()