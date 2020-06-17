from quantity_measurement.main.measurement import Measurement


class LengthData(Measurement):
	def __init__(self, unit, value):
		super().__init__(unit,value)

