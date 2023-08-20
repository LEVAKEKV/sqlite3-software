from db_func import DatabaseFunctions
from console_func import ConsoleFunctions


class UserSoftware:
	def __init__(self) -> None:
		"""Инициализируем объекты db и kf и работаем с ними"""
		self.db = DatabaseFunctions("storage_db.db")
		self.cf = ConsoleFunctions()

	def get_work_type(self) -> int:
		"""Получаем тип работы"""
		return self.cf.create_user_menu()

	def add_game(self) -> None:
		"""Добавляем игру"""
		name, year, owner = self.cf.add_game()
		self.db.create_game(name, year, owner)
		print("Игра успешно добавлена!")

	def search_game(self) -> None:
		"""Ищем игру"""
		search_query, search_type = self.cf.search_game()
		try:
			if search_type == 1:
				data = self.db.search_game_by_name(search_query)
			elif search_type == 2:
				data = self.db.search_game_by_year(int(search_query))
			else:
				data = self.db.search_game_by_owner(search_query)
			if data:
				data = data[0]
				text = ""
				for i in data:
					text += str(i) + ' '
				print(text)
			else:
				print("Не удалось ничего найти :(")
		except Exception as e:
			print(e)

	def get_all_games(self) -> None:
		"""Получаем все игры из базы"""
		text = ''
		for i in self.db.get_all_games():
			print(i[0] + ' ' + str(i[1]) + ' ' + i[2])
		print(text)
