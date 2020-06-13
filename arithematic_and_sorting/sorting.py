from utilities.Input import Input


class Sorter:
	def compute(self, number_1, number_2, number_3):
		return number_1 + number_2 * number_3



#driver code:
sorter = Sorter()
number1 = Input.get_input(int, "Enter 1st number ")
number2 = Input.get_input(int, "Enter 2nd number ")
number3 = Input.get_input(int, "Enter 3rd number ")
sorter.compute(number1,number2,number3)
print("%d + %d * %d = "%(number1,number2,number3),sorter.compute(number1,number2,number3))
