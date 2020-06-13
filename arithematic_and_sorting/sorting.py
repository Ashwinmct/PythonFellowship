import operator
from utilities.Input import Input


class Sorter:
	def compute(self, number1, number2, number3, operator1, operator2):
		return operator1(number1, operator2(number2, number3))



#driver code:
sorter = Sorter()
number1 = Input.get_input(int, "Enter 1st number ")
number2 = Input.get_input(int, "Enter 2nd number ")
number3 = Input.get_input(int, "Enter 3rd number ")
print("%d + ( %d * %d ) = " % (number1, number2, number3), sorter.compute(number1, number2, number3, operator.__add__, operator.__mul__))
print("%d * ( %d + %d ) = " % (number1, number2, number3), sorter.compute(number1, number2, number3, operator.__mul__, operator.__add__))
print("%d + ( %d / %d ) = " % (number1, number2, number3), sorter.compute(number1, number2, number3, operator.__add__, operator.__truediv__))
print("%d mod ( %d + %d ) = " % (number1, number2, number3), sorter.compute(number1, number2, number3, operator.__mod__, operator.__add__))
