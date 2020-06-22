import enum


class ClinicManagementError(Exception):
	class ExceptionType(enum.Enum):
		NOT_FOUND = "no person found for suitable for given details"

	def __init__(self,exception_type):
		self.exception_type = exception_type
