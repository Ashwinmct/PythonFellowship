from ..main.temperaturedata import TemperatureData
from ..main.measurement_units import MeasurementUnit
from ..main.measurement_exception import MeasurementError

class TestTemperature:
	def test_given_temperature_with_same_value_and_unit_when_equalised_should_return_true(self):
		temperature1 = TemperatureData(MeasurementUnit.CELSIUS, 1)
		temperature2 = TemperatureData(MeasurementUnit.CELSIUS, 1)
		assert temperature1.equals(temperature2)

	def test_given_temperature_with_zero_value_and_different_unit_when_equalised_should_return_false(self):
		temperature1 = TemperatureData(MeasurementUnit.CELSIUS, 0)
		temperature2 = TemperatureData(MeasurementUnit.FAHRENHEIT, 0)
		assert temperature1.equals(temperature2) is False

	def test_given_temperature_with_same_reference_when_equalised_should_return_true(self):
		temperature1 = TemperatureData(MeasurementUnit.CELSIUS, 1)
		temperature2 = temperature1
		assert temperature1.equals(temperature2)

	def test_given_temperature_with_invalid_unit_should_raise_exception(self):
		try:
			TemperatureData(MeasurementUnit.KILO_GRAM,1)
		except MeasurementError as err:
			assert MeasurementError.ExceptionType.INVALID_UNIT == err.exception_type

	def test_given_temperature_in_fahrenheit_and_its_respective_celsius_value_when_equalised_should_return_true(self):
		temperature1 = TemperatureData(MeasurementUnit.CELSIUS, 100)
		temperature2 = TemperatureData(MeasurementUnit.FAHRENHEIT, 212)
		assert temperature1.equals(temperature2)
