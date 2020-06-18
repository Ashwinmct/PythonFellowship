import enum
from .base_units import BaseUnit


class MeasurementUnit(enum.Enum):

	#for length
	INCH = {"type": BaseUnit.LENGTH, "BasicUnitConversionFactor": 1}
	FEET = {"type": BaseUnit.LENGTH, "BasicUnitConversionFactor": 12}
	YARD = {"type": BaseUnit.LENGTH, "BasicUnitConversionFactor": 36}
	CENTIMETER = {"type": BaseUnit.LENGTH, "BasicUnitConversionFactor": 0.4}
	#for volume
	GALLON = {"type": BaseUnit.VOLUME, "BasicUnitConversionFactor": 3.78}
	LITRE = {"type": BaseUnit.VOLUME, "BasicUnitConversionFactor": 1}
	MILLI_LITRE = {"type": BaseUnit.VOLUME, "BasicUnitConversionFactor": 0.001}
	#for mass
	KILO_GRAM = {"type": BaseUnit.MASS, "BasicUnitConversionFactor": 1}
	GRAM = {"type": BaseUnit.MASS, "BasicUnitConversionFactor": 0.001}
	TONNE = {"type": BaseUnit.MASS, "BasicUnitConversionFactor": 1000}

	def get_basic_unit_conversion_factor(self):
		return self.value.get("BasicUnitConversionFactor")

	def get_base_unit(self):
		return self.value.get("type")
