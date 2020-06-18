import enum


class MeasurementError(Exception):
	class ExceptionType(enum.Enum):
		INVALID_UNIT = "given unit is not suitable for this measurement"
		INVALID_ADDITION = "given measurements cant be added"

	def __init__(self, exception_type):
		self.exception_type = exception_type
