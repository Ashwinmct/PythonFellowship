

class BinaryOperations:
	@staticmethod
	def to_binary(number):
		bin_num = ''
		while number > 1:
			bin_num = str(number % 2) + bin_num
			number = number // 2
		return '1' + bin_num


#driver code
if __name__ == "__main__":
	number = 55
	binary_number = BinaryOperations.to_binary(number)
	print(binary_number)