from .measurement import Measurement
from .measurement_exception import MeasurementError
from .base_units import BaseUnit


class MassData(Measurement):
	quantity_type = BaseUnit.MASS

	def __init__(self, unit, value):
		if not unit.get_base_unit() == self.quantity_type:
			raise MeasurementError(MeasurementError.ExceptionType.INVALID_UNIT)
		super().__init__(unit, value)
