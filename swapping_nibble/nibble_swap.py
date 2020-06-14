

class BinaryOperations:
	@staticmethod
	def to_binary(number):
		binary_string = ''
		while number > 1:
			binary_string = str(number % 2) + binary_string
			number = number // 2
		return '1' + binary_string

	@classmethod
	def convert_to_nibble(cls, number):
		standard_nibble_length = 4
		binary_number = BinaryOperations.to_binary(number)
		if len(binary_number)%standard_nibble_length != 0:
			binary_number = (standard_nibble_length - len(binary_number) % standard_nibble_length) * '0' + binary_number
		return binary_number


#driver code
if __name__ == "__main__":
	number = 1
	binary_number = BinaryOperations.convert_to_nibble(number)
	print(binary_number)