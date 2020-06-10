#exception handling is used to handle exception as well as raise error
#except : used to catch any exception

def divide(number1, number2):
	try:
		result = number1 / number2
	except ZeroDivisionError:
		print("Divided by zero")
	finally:
		return result

print("divided value = ", divide(int(input("Enter a number ")), int(input("Enter another number "))))