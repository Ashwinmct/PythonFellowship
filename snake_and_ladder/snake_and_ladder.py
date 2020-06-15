import random
from utilities.Input import Input


class SnakeAndLadder:
	__BOARD_STARTING = 1
	__BOARD_END = 100

	def __init__(self):
		print("Welcome to SnakeAndLadder Game")
		if Input.get_input("Enter 0 if you want to simulate snake_and_ladder_game ", int) == 0:
			self.__play_game()
		print("Thank you")

	def __play_game(self):
		global player1_position, player2_position
		game_status = True
		player1_position = self.__BOARD_STARTING
		player2_position = self.__BOARD_STARTING
		dice_count = 0
		while [game_status]:
			player1_position = self.__get_position(player1_position)
			dice_count += 1
			player2_position = self.__get_position(player2_position)
			dice_count += 1
			if player1_position >= self.__BOARD_END or player2_position >= self.__BOARD_END:
				break
		print("Total dice rolls required: ", dice_count)

	def __get_dice_value(self, dice_value=0):
		dice_value += random.randint(1, 7)
		if dice_value % 6 == 0:
			return self.__get_dice_value(dice_value)
		return dice_value

	def __get_position(self, player_position):
		dice_value = self.__get_dice_value()
		player_position = player_position + dice_value
		return self.__BOARD_END if player_position >= self.__BOARD_END else self.__check_option(player_position)

	def __check_option(self, position):
		ladder_position = {1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99}
		snake_position = {32: 10, 36: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78}
		options_list = [ladder_position, snake_position]
		for option in options_list:
			for cell in option.keys():
				if cell == position:
					return option.get(cell)
		return position


#driver_code
snake_and_ladder = SnakeAndLadder()