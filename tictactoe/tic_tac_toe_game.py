
class TicTacToe:
	tic_tac_toe_board = [['', '', ''], ['', '', ''], ['', '', '']]

	def __init__(self):
		self.play_game()

	def reset_board(self):
		global tic_tac_toe_board
		tic_tac_toe_board = [['', '', ''], ['', '', ''], ['', '', '']]

	def play_game(self):
		self.reset_board()
		print("Welcome to the game")
		self.print_board()

	def print_board(self):
		global tic_tac_toe_board
		print("Your Board")
		for row in range(len(tic_tac_toe_board)):
			print("%s || %s || %s" % (tic_tac_toe_board[row][0], tic_tac_toe_board[row][1], tic_tac_toe_board[row][2]))


#driver code
tic_tac_toe = TicTacToe()