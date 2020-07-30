import random
from utilities.input import Input


class TicTacToe:
	__cells_occupied_list = []
	__EMPTY = ''
	__user = __EMPTY
	__computer = __EMPTY
	__NO_WINNER = "-1"
	__winner = __NO_WINNER
	__TOTAL_CELLS = 9
	__STARTING_CELL = 1
	__NO_CELL_VALUE = 0

	def __init__(self):
		if input(
				"Welcome to Tic Tac Toe \n do you like to play if yes enter 0 else enter any other number or character ") == '0':
			self.__play_game()
		print("Thank you")

	def __reset_board(self):
		global tic_tac_toe_board
		tic_tac_toe_board = [['', '', ''], ['', '', ''], ['', '', '']]

	def __play_game(self):
		self.__initialise_game()
		print("Game Started")
		self.__print_board()
		for cell in range(self.__TOTAL_CELLS):
			if cell % 2 == 0:
				self.__store_board(self.__get_input(player1), player1)
			else:
				self.__store_board(self.__get_input(player2), player2)
			self.__print_board()
			if self.__check_winner() != self.__NO_WINNER:
				self.__print_winner()
				break
		if self.__winner == self.__NO_WINNER:
			print("Match Tie")

	def __print_board(self):
		print("TicTacToe Board")
		for row in range(len(tic_tac_toe_board)):
			print("%s || %s || %s" % (tic_tac_toe_board[row][0], tic_tac_toe_board[row][1], tic_tac_toe_board[row][2]))

	def __initialise_game(self):
		self.__reset_board()
		print("Welcome to the game \nBoard Layout: \n 1 || 2 || 3 \n 4 || 5 || 6 \n 7 || 8 || 9 "
		      "\nEnter position you want as shown as above")
		self.__set_values()

	def __set_values(self):
		if random.randint(0, 1) == 0:
			self.__computer = 'x'
			self.__user = 'o'
		else:
			self.__computer = 'o'
			self.__user = 'x'
		print("You will be '%s' \n Computer will be '%s'" % (self.__user, self.__computer))
		self.__toss_game()

	def __toss_game(self):
		global player1, player2
		user_choice = Input.get_input("Enter your choice to toss '0' for HEAD or another number for Tail ", int)
		toss_result = random.randint(0, 1)
		if user_choice == toss_result:
			print('YOU won the toss')
			player1 = self.__user
			player2 = self.__computer
			return
		print("COMPUTER won the toss")
		player1 = self.__computer
		player2 = self.__user

	def __check_winner(self):
		###check rows
		for row in range(len(tic_tac_toe_board)):
			if tic_tac_toe_board[row][0] == tic_tac_toe_board[row][1] == tic_tac_toe_board[row][2] \
					and tic_tac_toe_board[row][0] != self.__EMPTY:
				return tic_tac_toe_board[row][0]

		###check columns
		for column in range(len(tic_tac_toe_board)):
			if tic_tac_toe_board[0][column] == tic_tac_toe_board[1][column] == tic_tac_toe_board[2][column] \
					and tic_tac_toe_board[0][column] != self.__EMPTY:
				return tic_tac_toe_board[0][column]

		###check principal diagonal
		if tic_tac_toe_board[0][0] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][2] \
				and tic_tac_toe_board[1][1] != self.__EMPTY:
			return tic_tac_toe_board[1][1]

		###check secondary diagonal
		if tic_tac_toe_board[0][2] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][0] \
				and tic_tac_toe_board[1][1] != self.__EMPTY:
			return tic_tac_toe_board[1][1]

		# if no winning combination is found
		return self.__NO_WINNER

	def __get_input(self, player):
		if self.__user == player:
			return self.__get_user_input()
		return self.__generate_computer_input()

	def __get_user_input(self):
		user_input = Input.get_input("Enter the position you want ", int)
		condition_dictionary = {
			user_input > self.__TOTAL_CELLS or user_input < self.__STARTING_CELL:
				"Entered Incorrect option \nPlease Enter Again",
			self.__cells_occupied_list.__contains__(user_input):
				"Entered Position Already Occupied \nPlease Enter Again "}
		for condition, message in condition_dictionary.items():
			if condition is True:
				print(message)
				return self.__get_user_input()
		self.__cells_occupied_list.append(user_input)
		return user_input

	def __store_board(self, position, player):
		cell_position = (position % 3) - 1
		if position <= 3:
			tic_tac_toe_board[0][cell_position] = player
			return
		if 3 < position <= 6:
			tic_tac_toe_board[1][cell_position] = player
			return
		if position > 6:
			tic_tac_toe_board[2][cell_position] = player
			return

	def __generate_computer_input(self):
		computer_move = self.__get_available_move()
		self.__cells_occupied_list.append(computer_move)
		return computer_move

	def __get_available_move(self):
		cell_priority_list = [1, 3, 7, 9, 5, 2, 4, 6, 8]
		players = [self.__computer, self.__user]
		board_details_list = self.__get_board_status()
		for player in players:
			move = self.__check_move(player, board_details_list)
			if not self.__cells_occupied_list.__contains__(move) and move != self.__NO_CELL_VALUE:
				return move

		for cell in cell_priority_list:
			if not cell in self.__cells_occupied_list:
				return cell

	def __check_move(self, player, board_list):
		cell_combination_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
		for cell_list in cell_combination_list:
			if(len(list(filter(lambda cell: board_list[cell] == player, cell_list)))) == 2:
				empty_cell = list(filter(lambda cell: board_list[cell] == self.__EMPTY, cell_list))
				if len(empty_cell) == 1:
					return empty_cell[0] + self.__STARTING_CELL

		return self.__NO_CELL_VALUE

	def __print_winner(self):
		self.__winner = "You" if(self.__check_winner() == self.__user) else "Computer"
		print("%s won the match" % self.__winner)

	def __get_board_status(self):
		board_list = []
		global tic_tac_toe_board
		for row in tic_tac_toe_board:
			for cell in row:
				board_list.append(cell)
		return board_list


# driver code
tic_tac_toe = TicTacToe()
