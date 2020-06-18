from .measurement import Measurement
from .measurement_exception import MeasurementError
from .basic_quantity import BasicQuantity
from .measurement_units import MeasurementUnit


class Mass(Measurement):
	quantity_type = BasicQuantity.MASS
	base_unit = MeasurementUnit.KILO_GRAM

	def __init__(self, unit, value):
		if not unit.get_base_unit() == self.quantity_type:
			raise MeasurementError(MeasurementError.ExceptionType.INVALID_UNIT)
		super().__init__(unit, value)

	def __add__(self, other):
		return Mass(self.base_unit, super().__add__(other))
