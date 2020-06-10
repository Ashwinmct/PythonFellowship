#Higher order function : function with other function as parameter
def apply_thrice(function, argument):
	return function(function(function(argument)))


#normal function
def multiply_by_two(number):
	return 2 * number


#pure_function : function which is only depend on arguments given
def add(number1, number2):
	return number1+number2


#lambda function : anonymous function  with single expression
add_three_numbers = lambda number1, number2, number3: number1 + number2 + number3


#driver code
num = int(input("Enter one no. "))
num2 = 8
print("value", apply_thrice(multiply_by_two, num))
print("added value = ", add(int(input("Enter another number : ")), num))
print(add_three_numbers(num, num2, int(input("Enter another number : "))))