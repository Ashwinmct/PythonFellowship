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
		if self.convert_to_basic_unit_value(self) == self.convert_to_basic_unit_value(obj):
			return True
		return False

	@staticmethod
	def convert_to_basic_unit_value(obj):
		return obj.value * obj.unit.get_basic_unit_conversion_factor()
