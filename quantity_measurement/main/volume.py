from .measurement import Measurement
from .measurement_exception import MeasurementError
from .basic_quantity import BasicQuantity
from .measurement_units import MeasurementUnit


class Volume(Measurement):
	quantity_type = BasicQuantity.VOLUME
	basic_unit = MeasurementUnit.LITRE

	def __init__(self, unit, value):
		if not unit.get_base_unit() is self.quantity_type:
			raise MeasurementError(MeasurementError.ExceptionType.INVALID_UNIT)
		super().__init__(unit, value)

	def __add__(self, other):
		return Volume(self.basic_unit, super().__add__(other))
