numbers_list = [11, 12, 13, 14, 15]

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

print("Example numbers list :", numbers_list)

#map function: takes a function and an iterable as parameter
map_function_result = list(map(multiply_by_two, numbers_list))
print("map function result ", map_function_result)

#filter function :used to filter values which doesnt match given condition
filter_function_result = list(filter(lambda number: number%2==0, numbers_list))
print("filter function result ", filter_function_result)

#Generator: little similar to iterator
def generate_number_list(number):
	for num in range(number):
		yield num

print(list(generate_number_list(int(input("Enter limit of list you want to generate ")))))