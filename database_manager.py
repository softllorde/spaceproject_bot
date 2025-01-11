import sqlite3

from player import Player
from spaceship import Spaceship

class Database_Manager:
	def __init__(self, db_name):
		self.conn = sqlite3.connect(f"db/{db_name}")
		self.cursor = self.conn.cursor()

	def checkUserInDataBase(self,user_id):
        query = "SELECT COUNT(*) FROM players WHERE id = ?"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()[0]
        return result > 0

    def add_user(self, id, name):
        if not self.checkUserInDataBase(id):
            query = "INSERT INTO players (id, name) VALUES (?, ?)"
            self.cursor.execute(query, (id, name))
            self.conn.commit()
            result = "Успешно зарегестрирован! Напиши /help и узнай команды бота"
        else:
            result = "Пользователь уже найден в базе данных!"
        return result

    def delete_user(self, id):
        if self.checkUserInDataBase(id):
            query = "DELETE FROM players WHERE id = ?"
            self.cursor.execute(query, (id,))
            self.conn.commit()
            result = "Пользователь успешно удален!"
        else:
            result = "Такого пользователя не существует"
        return result

    def get_player_info(self, player_id):
        self.cursor.execute("SELECT * FROM players WHERE id=?", (player_id,))
        player_data = self.cursor.fetchone()
        if player_data:
        	id,name,balance = player_data
        	return player_data
       	else:
       		return None

    def __del__(self):
        self.conn.close()