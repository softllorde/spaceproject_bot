import telebot
from player import Player

bot = telebot.TeleBot('7192017546:AAHmm8rgHh2sR_wHTYMh0pqS_5NWUPJRPGc',skip_pending=True)

@bot.message_handler()
def answer(message):
	if message.text == "Привет":
		user = Player(message.from_user.id, message.from_user.username, 100)
		bot.reply_to(message, "Player " + user.getUserName() + "\nUserID: " + str(user.getUserId()) + "\nBalance: " + str(user.getUserBalance()))

bot.infinity_polling()