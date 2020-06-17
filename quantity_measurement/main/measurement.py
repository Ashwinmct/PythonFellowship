import abc


class Measurement(abc.ABC):

	def __init__(self, unit, value):
		self.value = value
		self.unit = unit

	def equals(self, obj):
		if obj is None:
			return False
		if self == obj:
			return True
		if not isinstance(obj, Measurement):
			return False
		if self.value == obj.value and self.unit == obj.unit:
			return True
		return False




