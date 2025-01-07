import telebot
from player import Player
from spaceship import Spaceship

bot = telebot.TeleBot('7192017546:AAHmm8rgHh2sR_wHTYMh0pqS_5NWUPJRPGc', skip_pending=True)

@bot.message_handler()
def answer(message):
	if message.text == "Привет":
		user = Player(message.from_user.id, message.from_user.username, 100, Spaceship(1, "Newbie", "Фрегат", 5))
		bot.reply_to(message, "Player " + user.getName() + "\nUserID: " + str(user.getId()) + "\nBalance: " + str(user.getBalance()) + "\nSpaceship: " + user.getSpaceship().getName())

bot.infinity_polling()