from main_functions import UserSoftware


def main():
	"""Главная функция, запуск всех модулей"""
	uf = UserSoftware()
	work_type = uf.get_work_type()
	if work_type == 1:
		uf.add_game()
	elif work_type == 2:
		uf.search_game()
	else:
		uf.get_all_games()


if __name__ == "__main__":
	"""Запуск"""
	main()
