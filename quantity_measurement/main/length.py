from .measurement import Measurement
from .measurement_units import MeasurementUnit
from .measurement_exception import MeasurementError
from .base_units import BaseUnit


class LengthData(Measurement):
	basic_unit = MeasurementUnit.INCH
	quantity_type = BaseUnit.LENGTH

	def __init__(self, unit, value):
		a = unit.get_base_unit()
		if not unit.get_base_unit() == self.quantity_type:
			raise MeasurementError(MeasurementError.ExceptionType.INVALID_UNIT)
		super().__init__(unit, value)

	def __add__(self, other):
		return LengthData(self.basic_unit ,super().__add__(other))
