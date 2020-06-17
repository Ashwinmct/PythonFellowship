import enum


class MeasurementUnit(enum.Enum):
	class BaseUnit(enum.Enum):
		LENGTH = 1
	INCH = {"type": BaseUnit.LENGTH, "BasicUnitConversionFactor": 1}
	FEET = {"type": BaseUnit.LENGTH, "BasicUnitConversionFactor": 12}
	YARD = {"type": BaseUnit.LENGTH, "BasicUnitConversionFactor": 36}

	def get_basic_unit_conversion_factor(self):
		return self.value.get("BasicUnitConversionFactor")
