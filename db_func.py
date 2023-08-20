import sqlite3


class DatabaseFunctions:
	def __init__(self, db_path: str) -> None:
		"""Инициализация соединения и работа с БД"""
		self.connection = sqlite3.connect(db_path)
		self.cursor = self.connection.cursor()

	def create_table(self) -> None:
		"""Создаем таблицу storage_game"""
		with self.connection:
			self.cursor.execute("CREATE TABLE IF NOT EXISTS storage_games("
								"name TEXT,"
								"year ID,"
								"owner TEXT)")

	def create_game(self, name: str, year: int, owner: str) -> None:
		"""Добавляем игру в таблицу storage_game"""
		with self.connection:
			self.cursor.execute("INSERT INTO storage_games VALUES(?, ?, ?)", (name, year, owner))

	def search_game_by_name(self, name: str) -> list:
		"""Ищем игру по ее названию"""
		with self.connection:
			sql = "SELECT * FROM storage_games WHERE name = ?"
			return self.cursor.execute(sql, (name, )).fetchall()

	def search_game_by_year(self, year: int) -> list:
		"""Ищем игру по году издания"""
		with self.connection:
			sql = "SELECT * FROM storage_games WHERE year = ?"
			return self.cursor.execute(sql, (year, )).fetchall()

	def search_game_by_owner(self, owner: str) -> list:
		"""Ищем игру по ее разработчику"""
		with self.connection:
			sql = "SELECT * FROM storage_games WHERE owner = ?"
			return self.cursor.execute(sql, (owner,)).fetchall()

	def get_all_games(self) -> tuple:
		"""Получаем все игры"""
		with self.connection:
			sql = "SELECT * FROM storage_games"
			return self.cursor.execute(sql).fetchall()
