import pytest
from quantity_measurement.main.length import Length
from quantity_measurement.main.measurement_units import MeasurementUnit
from quantity_measurement.main.measurement_exception import MeasurementError


class TestMeasurement:
	def test_for_given_two_measurements_when_added_should_return_added_value(self):
		measurement1 = Length(MeasurementUnit.INCH, 1)
		measurement2 = Length(MeasurementUnit.YARD, 1)
		expected_value = Length(MeasurementUnit.INCH, 37)
		calculated_value = measurement1.__add__(measurement2)
		assert calculated_value.equals(expected_value)

	def test_for_given_two_measurements_of_different_type_when_added_should_throw_exception(self):
		try:
			measurement1 = Length(MeasurementUnit.INCH, 1)
			measurement2 = 2
			measurement1.__add__(measurement2)
		except MeasurementError as err:
			assert MeasurementError.ExceptionType.INVALID_ADDITION == err .exception_type

	def test_given_measurement_with_string_value_when_created_should_raise_exception(self):
		with pytest.raises(MeasurementError) as error:
			Length(MeasurementUnit.INCH, 'a')
			assert error.exception_type == MeasurementError.ExceptionType.INVALID_VALUE

	def test_given_measurement_with_boolean_value_when_created_should_raise_exception(self):
		with pytest.raises(MeasurementError) as error:
			Length(MeasurementUnit.FAHRENHEIT, True)
			assert error.exception_type == MeasurementError.ExceptionType.INVALID_VALUE
