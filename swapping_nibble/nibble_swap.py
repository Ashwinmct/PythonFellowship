

class BinaryOperations:
	@staticmethod
	def to_binary(number):
		binary_string = ''
		while number > 1:
			binary_string = str(number % 2) + binary_string
			number = number // 2
		return BinaryOperations.convert_to_nibble('1' + binary_string)


	@classmethod
	def convert_to_nibble(cls, binary_number):
		STANDARD_NIBBLE_LENGTH = 4
		if len(binary_number)%STANDARD_NIBBLE_LENGTH != 0:
			binary_number = (STANDARD_NIBBLE_LENGTH - len(binary_number) % STANDARD_NIBBLE_LENGTH) * '0' + binary_number
		return binary_number


#driver code
if __name__ == "__main__":
	number = 5
	binary_number = BinaryOperations.to_binary(number)
	print(binary_number)