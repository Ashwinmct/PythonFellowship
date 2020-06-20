from pincode_validation.pincode_validator import PinCodeValidator


class TestPinCodeValidation:
	def test_given_pin_code_with_exactly_6_digits_when_validated_should_return_true(self):
		pin_code_validator = PinCodeValidator()
		pin_code = 400088
		assert pin_code_validator.validate(pin_code)

	def test_given_pin_code_with_less_than_6_digits_when_validated_should_return_false(self):
		pin_code_validator = PinCodeValidator()
		pin_code = 4000
		assert pin_code_validator.validate(pin_code) is False

	def test_given_pin_code_with_more_than_6_digits_when_validated_should_return_false(self):
		pin_code_validator = PinCodeValidator()
		pin_code = 4001088
		assert pin_code_validator.validate(pin_code) is False

	def test_given_pin_code_with_charecter_other_than_digit_should_return_false(self):
		pin_code_validator = PinCodeValidator()
		pin_code = "asd123"
		assert pin_code_validator.validate(pin_code) is False

	def test_given_pin_code_starts_with_zero_when_validated_should_return_false(self):
		pin_code_validator = PinCodeValidator()
		pin_code = "000088"
		assert pin_code_validator.validate(pin_code) is False

	def test_given_pin_code_with_space_in_between_when_validated_should_return_true(self):
		pin_code_validator = PinCodeValidator()
		pin_code = "400 088"
		assert pin_code_validator.validate(pin_code)
