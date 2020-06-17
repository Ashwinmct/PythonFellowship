import enum


class MeasurementUnit(enum.Enum):
	class BaseUnit(enum.Enum):
		LENGTH = 1
	INCH = {"type": BaseUnit.LENGTH, "BasicUnitConversion": 1}
