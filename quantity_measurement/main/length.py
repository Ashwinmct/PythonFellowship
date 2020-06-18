from .measurement import Measurement
from .measurement_units import MeasurementUnit


class LengthData(Measurement):
	basic_unit = MeasurementUnit.INCH

	def __init__(self, unit, value):
		super().__init__(unit, value)

	def __add__(self, other):
		return LengthData(self.basic_unit ,super().__add__(other))
