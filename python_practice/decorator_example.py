def decorator_hello(fun):
	def add_hello(name):
		return "Hi All! This is %s"%name
	return add_hello

@decorator_hello
def print_hello_message(name):
	return name

#driver code
print(print_hello_message(input("Enter your name\n")))