import random


class Input:

	@staticmethod
	def get_input(message, input_type):
		try:
			value = input_type(input(message))
			return value
		except ValueError:
			print(" Wrong type of value Entered, Enter again")
			return Input.get_input(message, input_type)


class TicTacToe:
	tic_tac_toe_board = [['', '', ''], ['', '', ''], ['', '', '']]
	user = ''
	computer = ''
	player1 = ''
	player2 = ''
	no_winner = "-1"

	def __init__(self):
		if input(
				"Welcome to Tic Tac Toe \n do you like to play if yes enter 0 else enter any other number or character ") == '0':
			self.play_game()
		else:
			print("Thank you")

	def reset_board(self):
		global tic_tac_toe_board
		tic_tac_toe_board = [['', '', ''], ['', '', ''], ['', '', '']]

	def play_game(self):
		self.initialise_game()
		self.print_board()

	def print_board(self):
		global tic_tac_toe_board
		print("Your Board")
		for row in range(len(tic_tac_toe_board)):
			print("%s || %s || %s" % (tic_tac_toe_board[row][0], tic_tac_toe_board[row][1], tic_tac_toe_board[row][2]))

	def initialise_game(self):
		self.reset_board()
		print("Welcome to the game \nBoard Layout: \n 1 || 2 || 3 \n 4 || 5 || 6 \n 7 || 8 || 9")
		print("Enter position you want as shown as above")
		self.set_values()

	def set_values(self):
		global user, computer
		if random.randint(0, 1) == 0:
			print("You will be 'O' \n Computer will be 'X' ")
			computer = str('x')
			user = str('o')
		else:
			print("You will be 'X' \n Computer will be 'O' ")
			computer = str('o')
			user = str('x')
		self.toss_game()

	def toss_game(self):
		user_choice = Input.get_input("Enter your choice to toss '0' for HEAD and '1' for Tail ", int)
		toss_result = random.randint(0, 1)
		if user_choice == toss_result:
			print('YOU won the toss')
			self.player1 = self.user
			self.player2 = self.computer
			return
		else:
			print("COMPUTER won the toss")
			self.player1 = self.computer
			self.player2 = self.user

	def check_winner(self):
		###check rows
		for row in range(len(tic_tac_toe_board)):
			if tic_tac_toe_board[row][0] == tic_tac_toe_board[row][1] == tic_tac_toe_board[row][2] and tic_tac_toe_board[row][0] != '':
				return tic_tac_toe_board[row][0]

		###check columns
		for column in range(len(tic_tac_toe_board)):
			if tic_tac_toe_board[column][0] == tic_tac_toe_board[column][1] == tic_tac_toe_board[column][2] and tic_tac_toe_board[column][0] != '':
				return tic_tac_toe_board[column][0]

		###check pricipal diagonal
		for column in range(len(tic_tac_toe_board)):
			if tic_tac_toe_board[0][0] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][2] and tic_tac_toe_board[1][1] != '':
				return tic_tac_toe_board[1][1]

		###check pricipal diagonal
		for column in range(len(tic_tac_toe_board)):
			if tic_tac_toe_board[0][1] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][0] and tic_tac_toe_board[1][1] != '':
				return tic_tac_toe_board[1][1]

		#if no winning combination is found
		return self.no_winner

# driver code
tic_tac_toe = TicTacToe()
