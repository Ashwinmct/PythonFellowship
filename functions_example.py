#Higher order function : function with other function as parameter
def apply_thrice(function,argument):
	return function(function(function(argument)))

#normal function
def multiply_by_two(number):
	return 2 * number

#pure_function : function which is only depend on arguments given
def pure_function_example(number1, number2):
	return number1+number2


#driver code
num=int(input("Enter one no. "))
print("value", apply_thrice(multiply_by_two, num))
print("added value = ", pure_function_example(int(input("Enter another number : ")), num))