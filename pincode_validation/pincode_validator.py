import re


class PinCodeValidator:
	PIN_CODE_PATTERN = "\d{6}"

	def validate(self, pin_code):
		return True if(re.fullmatch(self.PIN_CODE_PATTERN, str(pin_code))) else False
