from .measurement import Measurement
from .measurement_units import MeasurementUnit
from .measurement_exception import MeasurementError
from .basic_quantity import BasicQuantity


class Length(Measurement):
	basic_unit = MeasurementUnit.INCH
	quantity_type = BasicQuantity.LENGTH

	def __init__(self, unit, value):
		if not unit.get_base_unit() == self.quantity_type:
			raise MeasurementError(MeasurementError.ExceptionType.INVALID_UNIT)
		super().__init__(unit, value)

	def __add__(self, other):
		return Length(self.basic_unit, super().__add__(other))
