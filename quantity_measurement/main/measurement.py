import abc


class Measurement(abc.ABC):

	def __init__(self, value):
		self.value = value

	def equals(self, obj):
		if obj is None:
			return False
		if self == obj:
			return True
		if not isinstance(obj, Measurement):
			return False
		measurement = Measurement(obj)
		if self.value == measurement.value.value:
			return True
		return False




