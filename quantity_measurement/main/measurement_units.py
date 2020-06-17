import enum


class MeasurementUnit(enum.Enum):
	class BaseUnit(enum.Enum):
		LENGTH = 1
	INCH = {"type": BaseUnit.LENGTH, "BasicUnitConversion": 1}
	FEET = {"type": BaseUnit.LENGTH, "BasicUnitConversion": 12}
	YARD = {"type": BaseUnit.LENGTH, "BasicUnitConversion": 36}
