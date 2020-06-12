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
	board_status_list = []
	tic_tac_toe_board = [['', '', ''], ['', '', ''], ['', '', '']]
	user = ''
	computer = ''
	player1 = ''
	player2 = ''
	NO_WINNER = "-1"
	TOTAL_CELLS = 9
	STARTING_CELL = 1

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
		global player1, player2
		for cell in range(self.TOTAL_CELLS):
			if cell % 2 == 0:
				player_input = self.get_input(player1)
				self.store_board(player_input, player1)
		self.initialise_game()
		self.print_board()

	def print_board(self):
		global tic_tac_toe_board
		print("Your Board")
		for row in range(len(tic_tac_toe_board)):
			print("%s || %s || %s" % (tic_tac_toe_board[row][0], tic_tac_toe_board[row][1], tic_tac_toe_board[row][2]))

	def initialise_game(self):
		self.reset_board()
		print("Welcome to the game \nBoard Layout: \n 1 || 2 || 3 \n 4 || 5 || 6 \n 7 || 8 || 9 "
		      "\nEnter position you want as shown as above")
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
			if tic_tac_toe_board[row][0] == tic_tac_toe_board[row][1] == tic_tac_toe_board[row][2] \
					and tic_tac_toe_board[row][0] != '':
				return tic_tac_toe_board[row][0]

		###check columns
		for column in range(len(tic_tac_toe_board)):
			if tic_tac_toe_board[column][0] == tic_tac_toe_board[column][1] == tic_tac_toe_board[column][2] \
					and tic_tac_toe_board[column][0] != '':
				return tic_tac_toe_board[column][0]

		###check principal diagonal
		if tic_tac_toe_board[0][0] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][2] \
				and tic_tac_toe_board[1][1] != '':
			return tic_tac_toe_board[1][1]

		###check secondary diagonal
		if tic_tac_toe_board[0][1] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][0] \
				and tic_tac_toe_board[1][1] != '':
			return tic_tac_toe_board[1][1]

		# if no winning combination is found
		return self.NO_WINNER

	def get_input(self, player):
		if user == player:
			return self.get_user_input()

	def get_user_input(self):
		global board_status_list, STARTING_CELL
		user_input = Input.get_input("Enter the position you want", int)
		if self.board_status_list.__contains__(user_input) and (user_input > self.TOTAL_CELLS or user_input < STARTING_CELL):
			print("Entered Incorrect option \nPlease Enter Again")
			return self.get_user_input()
		return user_input

	def store_board(self, position, player):
		cell_position = position % 3
		if position <= 3:
			tic_tac_toe_board[0][cell_position] = player
			return
		if 3 < position <= 6:
			tic_tac_toe_board[1][cell_position] = player
			return
		if position > 6:
			tic_tac_toe_board[2][cell_position] = player
			return


# driver code
tic_tac_toe = TicTacToe()
