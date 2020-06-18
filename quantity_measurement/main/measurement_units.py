import enum


class MeasurementUnit(enum.Enum):
	class BaseUnit(enum.Enum):
		LENGTH = 1
		VOLUME = 2

	#for length
	INCH = {"type": BaseUnit.LENGTH, "BasicUnitConversionFactor": 1}
	FEET = {"type": BaseUnit.LENGTH, "BasicUnitConversionFactor": 12}
	YARD = {"type": BaseUnit.LENGTH, "BasicUnitConversionFactor": 36}
	CENTIMETER = {"type": BaseUnit.LENGTH, "BasicUnitConversionFactor": 0.4}
	#for volume
	GALLON = {"type": BaseUnit.VOLUME, "BasicUnitConversionFactor": 3.78}
	LITRE = {"type": BaseUnit.VOLUME, "BasicUnitConversionFactor": 1}
	MILLI_LITRE = {"type": BaseUnit.VOLUME, "BasicUnitConversionFactor": 1000}

	def get_basic_unit_conversion_factor(self):
		return self.value.get("BasicUnitConversionFactor")
