import enum
from .basic_quantity import BasicQuantity


class MeasurementUnit(enum.Enum):

	#for length
	INCH = {"type": BasicQuantity.LENGTH, "BasicUnitConversionFactor": 1}
	FEET = {"type": BasicQuantity.LENGTH, "BasicUnitConversionFactor": 12}
	YARD = {"type": BasicQuantity.LENGTH, "BasicUnitConversionFactor": 36}
	CENTIMETER = {"type": BasicQuantity.LENGTH, "BasicUnitConversionFactor": 0.4}
	#for volume
	GALLON = {"type": BasicQuantity.VOLUME, "BasicUnitConversionFactor": 3.78}
	LITRE = {"type": BasicQuantity.VOLUME, "BasicUnitConversionFactor": 1}
	MILLI_LITRE = {"type": BasicQuantity.VOLUME, "BasicUnitConversionFactor": 0.001}
	#for mass
	KILO_GRAM = {"type": BasicQuantity.MASS, "BasicUnitConversionFactor": 1}
	GRAM = {"type": BasicQuantity.MASS, "BasicUnitConversionFactor": 0.001}
	TONNE = {"type": BasicQuantity.MASS, "BasicUnitConversionFactor": 1000}
	#for temperature
	CELSIUS = {"type": BasicQuantity.TEMPERATURE, "BasicUnitConversionFactor": 1.8}
	FAHRENHEIT = {"type": BasicQuantity.TEMPERATURE, "BasicUnitConversionFactor": 1}

	def get_basic_unit_conversion_factor(self):
		return self.value.get("BasicUnitConversionFactor")

	def get_base_unit(self):
		return self.value.get("type")
