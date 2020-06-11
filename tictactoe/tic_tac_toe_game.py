import random


class TicTacToe:
	tic_tac_toe_board = [['', '', ''], ['', '', ''], ['', '', '']]
	user = ''
	computer = ''
	
	
	def __init__(self):
		self.initialise_game()
		self.play_game()

	def reset_board(self):
		global tic_tac_toe_board
		tic_tac_toe_board = [['', '', ''], ['', '', ''], ['', '', '']]

	def play_game(self):
		self.reset_board()
		self.print_board()

	def print_board(self):
		global tic_tac_toe_board
		print("Your Board")
		for row in range(len(tic_tac_toe_board)):
			print("%s || %s || %s" % (tic_tac_toe_board[row][0], tic_tac_toe_board[row][1], tic_tac_toe_board[row][2]))

	def initialise_game(self):
		print("Welcome to the game \nBoard Layout: \n 1 || 2 || 3 \n 4 || 5 || 6 \n 7 || 8 || 9")
		print("Enter position you want as shown as above")
		self.set_values()


	def set_values(self):
		global user, computer
		if random.randint(0,1) == 0:
			print("You will be 'O' \n Computer will be 'X' ")
			computer = str('x')
			user = str('o')
		else:
			print("You will be 'X' \n Computer will be 'O' ")
			computer = str('o')
			user = str('x')



#driver code
tic_tac_toe = TicTacToe()