from utilities.Input import Input


class Sorter:
	def __init__(self):
		Sorter.take_input()

	@classmethod
	def take_input(cls):
		number1 = Input.get_input(int, "Enter 1st number ")
		number2 = Input.get_input(int, "Enter 2nd number ")
		number3 = Input.get_input(int, "Enter 3rd number ")


#driver code:
sorter = Sorter()



