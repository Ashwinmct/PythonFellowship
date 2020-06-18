from .measurement import Measurement


class VolumeData(Measurement):
	def __init__(self,unit,value):
		super().__init__(unit, value)
