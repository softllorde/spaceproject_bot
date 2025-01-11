import telebot
from player import Player
from spaceship import Spaceship
from database_manager import Database_Manager

bot = telebot.TeleBot('7192017546:AAHmm8rgHh2sR_wHTYMh0pqS_5NWUPJRPGc', skip_pending=True)

@bot.message_handler()
def answer(message):
	if message.text == "Привет":
		db = Database_Manager("database.db")
		bot.reply_to(message, db.add_user(message.from_user.id, message.from_user.first_name))

	if message.text == "Инфо":
		db = Database_Manager("database.db")
		player_data = db.get_player_info(message.from_user.id)
		id, name, balance = player_data
		spaceship = db.get_player_spaceship(message.from_user.id)
		spaceship_id, spaceship_name, spaceship_type, spaceship_hold_capacity, spaceship_attack, spaceship_defence = spaceship
		bot.reply_to(message, f"Character:\n\nID: {id}\nName: {name}\nBalance: {balance}\n\nSpaceship:\n\nName: {spaceship_name}\nType: {spaceship_type}\nHold Capacity: {spaceship_hold_capacity}\nAttack: {spaceship_attack}\nDefence: {spaceship_defence}")

bot.infinity_polling()