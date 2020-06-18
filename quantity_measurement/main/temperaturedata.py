from .measurement import Measurement
from .measurement_units import MeasurementUnit
from .measurement_units import BasicQuantity
from .measurement_exception import MeasurementError


class TemperatureData(Measurement):
	quantity_type = BasicQuantity.TEMPERATURE

	def __init__(self, unit, value):
		if not unit.get_base_unit() == self.quantity_type:
			raise MeasurementError(MeasurementError.ExceptionType.INVALID_UNIT)
		super().__init__(unit, value)

	@staticmethod
	def convert_to_basic_unit_value(obj):
		if obj.unit == MeasurementUnit.CELSIUS:
			return (obj.value * obj.unit.get_basic_unit_conversion_factor()) + 32
		return obj.value

