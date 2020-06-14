import random


class SnakeAndLadder:
	BOARD_STARTING = 1
	BOARD_END = 100
	game_status = True

	def __init__(self):
		self.__play_game()

	def __play_game(self):
		player1_position = self.BOARD_STARTING
		player2_position = self.BOARD_END
		while [self.game_status]:
			player1_position = self.__get_position(player1_position)
			player2_position = self.__get_position(player2_position)

	def __get_dice_value(self, dice_value=0):
		dice_value += self.__roll_dice()
		if dice_value % 6 == 0:
			return self.__get_dice_value(dice_value)
		return dice_value

	def __roll_dice(self):
		return random.randint(1,6)

	def __get_position(self, player_position):
		dice_value = self.__get_dice_value()
		return self.__check_option(player_position + dice_value)

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