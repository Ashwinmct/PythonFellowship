import random
from utilities.input import Input


class TicTacToe:
	board_status_list = []
	tic_tac_toe_board = [['', '', ''], ['', '', ''], ['', '', '']]
	user = ''
	computer = ''
	player1 = ''
	player2 = ''
	NO_WINNER = "-1"
	winner = NO_WINNER
	TOTAL_CELLS = 9
	STARTING_CELL = 1
	CORNERS = [1, 3, 7, 9]
	CENTER_CELL = 5
	SIDES = [2, 4, 6, 8]
	EMPTY = ''
	EMPTY_CELL_VALUE = 0

	def __init__(self):
		if input(
				"Welcome to Tic Tac Toe \n do you like to play if yes enter 0 else enter any other number or character ") == '0':
			self.play_game()
		print("Thank you")

	def reset_board(self):
		global tic_tac_toe_board
		tic_tac_toe_board = [['', '', ''], ['', '', ''], ['', '', '']]

	def play_game(self):
		self.initialise_game()
		print("Game Started")
		self.print_board()
		for cell in range(self.TOTAL_CELLS):
			if cell % 2 == 0:
				self.store_board( self.get_input(self.player1), self.player1)
			else:
				self.store_board( self.get_input(self.player2), self.player2)
			self.print_board()
			if (self.check_winner() != self.NO_WINNER):
				self.print_winner()
				break
		if (self.winner == self.NO_WINNER):
			print("Match Tie")

	def print_board(self):
		global tic_tac_toe_board
		print("TicTacToe Board")
		for row in range(len(tic_tac_toe_board)):
			print("%s || %s || %s" % (tic_tac_toe_board[row][0], tic_tac_toe_board[row][1], tic_tac_toe_board[row][2]))

	def initialise_game(self):
		self.reset_board()
		print("Welcome to the game \nBoard Layout: \n 1 || 2 || 3 \n 4 || 5 || 6 \n 7 || 8 || 9 "
		      "\nEnter position you want as shown as above")
		self.set_values()

	def set_values(self):
		if random.randint(0, 1) == 0:
			self.computer = 'x'
			self.user = 'o'
		else:
			self.computer = 'o'
			self.user = 'x'
		print("You will be '%s' \n Computer will be '%s'" %(self.user, self.computer))
		self.toss_game()

	def toss_game(self):
		global player1, player2
		user_choice = Input.get_input("Enter your choice to toss '0' for HEAD or another number for Tail ", int)
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
			if tic_tac_toe_board[0][column] == tic_tac_toe_board[1][column] == tic_tac_toe_board[2][column] \
					and tic_tac_toe_board[0][column] != '':
				return tic_tac_toe_board[0][column]

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
		if self.user == player:
			return self.get_user_input()
		return self.generate_computer_input()

	def get_user_input(self):
		user_input = Input.get_input("Enter the position you want ", int)
		if self.board_status_list.__contains__(user_input) or (user_input > self.TOTAL_CELLS or user_input < self.STARTING_CELL):
			print("Entered Incorrect option \nPlease Enter Again ")
			return self.get_user_input()
		self.board_status_list.append(user_input)
		return user_input

	def store_board(self, position, player):
		global tic_tac_toe_board
		cell_position = (position % 3) -1
		if position <= 3:
			tic_tac_toe_board[0][cell_position] = player
			return
		if 3 < position <= 6:
			tic_tac_toe_board[1][cell_position] = player
			return
		if position > 6:
			tic_tac_toe_board[2][cell_position] = player
			return

	def generate_computer_input(self):
		computer_move = self.check_available_moves()
		self.board_status_list.append(computer_move)
		return computer_move

	def check_available_moves(self):
		# check winning move
		winning_move = self.check_move(self.computer)
		if winning_move != self.EMPTY_CELL_VALUE:
			return winning_move
		# check blocking move
		blocking_move = self.check_move(self.user)
		if blocking_move != self.EMPTY_CELL_VALUE:
			return blocking_move
		#check corners
		for cell in self.CORNERS:
			if not self.board_status_list.__contains__(cell):
				return cell
		#check_centre
		if not self.board_status_list.__contains__(self.CENTER_CELL):
			return self.CENTER_CELL
		#check sides
		for cell in self.SIDES:
			if not self.board_status_list.__contains__(cell):
				return cell

	def check_move(self, player):
		middle_cell = len(tic_tac_toe_board) % 2
		middle_cell_value = self.TOTAL_CELLS // 2
		### check rows
		for row in range(len(tic_tac_toe_board)):
			if tic_tac_toe_board[row][0] == tic_tac_toe_board[row][1] == player and tic_tac_toe_board[row][2] == self.EMPTY:
				return row + 3
			if tic_tac_toe_board[row][0] == tic_tac_toe_board[row][2] == player and tic_tac_toe_board[row][1] == self.EMPTY:
				return row + 2
			if tic_tac_toe_board[row][1] == tic_tac_toe_board[row][2] == player and tic_tac_toe_board[row][0] == self.EMPTY:
				return row + 1
		### check column
		for column in range(len(tic_tac_toe_board)):
			if tic_tac_toe_board[0][column] == tic_tac_toe_board[1][column] == player and tic_tac_toe_board[2][column] == self.EMPTY:
				return column + 3
			if tic_tac_toe_board[0][column] == tic_tac_toe_board[2][column] == player and tic_tac_toe_board[1][column] == self.EMPTY:
				return column + 2
			if tic_tac_toe_board[1][column] == tic_tac_toe_board[2][column] == player and tic_tac_toe_board[0][column] == self.EMPTY:
				return column + 1
		### for diagonals
		if tic_tac_toe_board[middle_cell][middle_cell] == player == tic_tac_toe_board[middle_cell - 1][middle_cell - 1] \
				and tic_tac_toe_board[middle_cell+1][middle_cell+1] == self.EMPTY :
			return middle_cell_value + 4
		if tic_tac_toe_board[middle_cell][middle_cell] == player == tic_tac_toe_board[middle_cell + 1][middle_cell + 1] \
				and tic_tac_toe_board[middle_cell-1][middle_cell-1] == self.EMPTY :
			return middle_cell_value - 4
		if tic_tac_toe_board[middle_cell - 1][middle_cell - 1] == player == tic_tac_toe_board[middle_cell + 1][middle_cell + 1] \
				and tic_tac_toe_board[middle_cell][middle_cell] == self.EMPTY :
			return middle_cell_value
		if tic_tac_toe_board[middle_cell][middle_cell] == player == tic_tac_toe_board[middle_cell - 1][middle_cell + 1] \
				and tic_tac_toe_board[middle_cell+1][middle_cell-1] == self.EMPTY :
			return middle_cell_value + 2
		if tic_tac_toe_board[middle_cell][middle_cell] == player == tic_tac_toe_board[middle_cell + 1][middle_cell - 1] \
				and tic_tac_toe_board[middle_cell-1][middle_cell + 1] == self.EMPTY :
			return middle_cell_value - 2
		if tic_tac_toe_board[middle_cell - 1][middle_cell + 1] == player == tic_tac_toe_board[middle_cell + 1][middle_cell + 1] \
				and tic_tac_toe_board[middle_cell][middle_cell] == self.EMPTY:
			return middle_cell_value
		return self.EMPTY_CELL_VALUE

	def print_winner(self):
		self.winner = "You" if(self.check_winner() == self.user) else "Computer"
		print("%s won the match" % self.winner)


# driver code
tic_tac_toe = TicTacToe()
