from .measurement import Measurement
from .measurement_exception import MeasurementError
from .base_units import BaseUnit
from .measurement_units import MeasurementUnit


class VolumeData(Measurement):
	quantity_type = BaseUnit.VOLUME
	basic_unit = MeasurementUnit.LITRE

	def __init__(self, unit, value):
		if not unit.get_base_unit() is self.quantity_type:
			raise MeasurementError(MeasurementError.ExceptionType.INVALID_UNIT)
		super().__init__(unit, value)

	def __add__(self, other):
		return VolumeData(self.basic_unit, super().__add__(other))
