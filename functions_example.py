#Higher order function : fuction with other function as parameter
def apply_thrice(function,argument):
	return function(function(function(argument)))

#normal function
def multiply_by_two(number):
	return 2 * number

#driver code
num=int(input("Enter the no. "))
print("value", apply_thrice(multiply_by_two, num))