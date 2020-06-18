from .measurement import Measurement
from .measurement_units import MeasurementUnit
from .measurement_exception import MeasurementError
from .base_units import BaseUnit


class VolumeData(Measurement):
	quantity_type = BaseUnit.VOLUME

	def __init__(self, unit, value):
		if not unit.get_base_unit() is self.quantity_type:
			raise MeasurementError(MeasurementError.ExceptionType.INVALID_UNIT)
		super().__init__(unit, value)
