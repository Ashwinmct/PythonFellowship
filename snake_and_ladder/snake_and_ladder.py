import random


class SnakeAndLadder:
	def __init__(self):
		self.__start_game()

	def __start_game(self):
		print(self.__get_dice_value())

	def __get_dice_value(self, dice_value=0):
		dice_value += self.__roll_dice()
		if dice_value % 6 == 0:
			return self.__get_dice_value(dice_value)
		return dice_value

	def __roll_dice(self):
		return random.randint(1,6)


snake_and_ladder = SnakeAndLadder()