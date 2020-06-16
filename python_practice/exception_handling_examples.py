# exception handling is used to handle exception as well as raise error
# except : used to catch any exception

def divide(number1, number2):
	try:
		result = number1 / number2
		return result
	except ZeroDivisionError as err:
		print("Divided by zero", err)


print("divided value = ", divide(int(input("Enter a number ")), int(input("Enter another number "))))
