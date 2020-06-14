import enum
from utilities.Input import Input
from swapping_nibble.BinaryConversionException import BinaryConversionError

class Binary:

	class ConvertingOption(enum.Enum):
		nibble = 1
		byte = 2

	@staticmethod
	def to_binary(number):
		binary_string = ''
		while number > 1:
			binary_string = str(number % 2) + binary_string
			number = number // 2
		binary_string = '1' + binary_string
		return Binary.convert_to(Binary.ConvertingOption.nibble, binary_string)

	@classmethod
	def swap_nibbles(cls, binary_number):
		given_binary_number_in_byte = Binary.convert_to(Binary.ConvertingOption.byte, binary_number)
		splitting_value = len(given_binary_number_in_byte) // 2
		swapped_number = given_binary_number_in_byte[splitting_value::] + given_binary_number_in_byte[:splitting_value:]
		return swapped_number

	@classmethod
	def convert_to(cls, binary_type, binary_number):
		TYPE_CONVERSION_DETAILS = {Binary.ConvertingOption.byte: 8, Binary.ConvertingOption.nibble: 4}
		conversion_value = TYPE_CONVERSION_DETAILS.get(binary_type)
		if len(binary_number) % conversion_value != 0:
			binary_number = (conversion_value - len(binary_number) % conversion_value) * '0' + binary_number
		return binary_number

	@classmethod
	def to_Decimal(cls, binary_number):
		number = 0
		power = len(binary_number) - 1
		for value in binary_number:
			number += int(value)*(2**power)
			power -= 1
		return number


#driver code
if __name__ == "__main__":
	number = Input.get_input("Enter integer you want to convert to binary\n", int)
	binary_number = Binary.to_binary(number)
	print("%d in binary value" % number, binary_number)
	binary_number_after_swap = Binary.swap_nibbles(binary_number)
	print("Binary number after swapping", binary_number_after_swap)
	print("%s in decimal format" % binary_number_after_swap, Binary.to_Decimal(binary_number_after_swap))
