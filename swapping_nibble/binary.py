import enum
from utilities.Input import Input
from swapping_nibble.binary_conversion_exception import BinaryConversionError


class Binary:

	class ConvertingOption(enum.Enum):
		nibble = 1
		byte = 2

	@staticmethod
	def to_binary(number):
		Binary.__check_value(number)
		binary_string = ''
		while number > 1:
			binary_string = str(number % 2) + binary_string
			number = number // 2
		binary_string = '0' if number <= 0 else '1' + binary_string
		return Binary.__convert_to(Binary.ConvertingOption.nibble, binary_string)

	@classmethod
	def swap_nibbles(cls, binary_number):
		Binary.__check_value(binary_number, 2)
		given_binary_number_in_byte = Binary.__convert_to(Binary.ConvertingOption.byte, binary_number)
		splitting_value = len(given_binary_number_in_byte) // 2
		swapped_number = given_binary_number_in_byte[splitting_value::] + given_binary_number_in_byte[:splitting_value:]
		return swapped_number

	@classmethod
	def __convert_to(cls, binary_type, binary_number):
		TYPE_CONVERSION_DETAILS = {Binary.ConvertingOption.byte: 8, Binary.ConvertingOption.nibble: 4}
		conversion_value = TYPE_CONVERSION_DETAILS.get(binary_type)
		if len(binary_number) % conversion_value != 0:
			binary_number = (conversion_value - len(binary_number) % conversion_value) * '0' + binary_number
		return binary_number

	@classmethod
	def to_decimal(cls, binary_number):
		Binary.__check_value(binary_number, 2)
		number = 0
		power = len(binary_number) - 1
		for value in binary_number:
			number += int(value)*(2**power)
			power -= 1
		return number

	@classmethod
	def __check_value(cls, value, base=10):
		try:
			return int(str(value), base)
		except ValueError:
			raise BinaryConversionError("Invalid Value")


#driver code
if __name__ == "__main__":
	number = Input.get_input("Enter integer you want to convert to binary\n", int)
	binary_number = Binary.to_binary(number)
	print("%d in binary value" % number, binary_number)
	binary_number_after_swap = Binary.swap_nibbles(binary_number)
	print("Binary number after swapping", binary_number_after_swap)
	print("%s in decimal format" % binary_number_after_swap, Binary.to_decimal(binary_number_after_swap))
	try:
		binary_number = Binary.to_binary("a")
	except BinaryConversionError as err:
		print(err)

	try:
		binary_number = Binary.swap_nibbles("a")
	except BinaryConversionError as err:
		print(err)

	try:
		binary_number = Binary.to_decimal("a")
	except BinaryConversionError as err:
		print(err)