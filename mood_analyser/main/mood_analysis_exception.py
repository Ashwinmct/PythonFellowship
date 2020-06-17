import enum


class MoodAnalysisException(Exception):
	class ExceptionType(enum.Enum):
		NULL = "null data detected"
		EMPTY = "entered empty string"

	def __init__(self, exception_type):
		self.exception_type = exception_type
