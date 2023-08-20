class ConsoleFunctions:
	def create_user_menu(self) -> int:
		"""Генерируем главное меню для юзера"""
		print("Добро пожаловать в наше приложение!\n"
			  "1. Добавить игру\n"
			  "2. Найти игру\n"
			  "3. Просмотреть все игры\n")
		work_type = int(input("Выберите необходимую функцию: "))
		return work_type

	def add_game(self) -> tuple[str, int, str]:
		"""Добавляем игру от юзера"""
		game_name = input("Введите название игры: ")
		game_year = int(input("Введите год издания игры: "))
		game_owner = input("Введите имя разработчика игры: ")
		return game_name, game_year, game_owner

	def search_game(self) -> tuple[str, int]:
		"""Ищем игру по параметрам от юзера"""
		search_query = input("Введите запрос: ")
		print("1. Искать игру по названию\n"
			  "2. Искать игру по году издания\n"
			  "3. Искать игру по разработчику")
		work_type = int(input("Выберите необходимую функцию: "))
		return search_query, work_type
