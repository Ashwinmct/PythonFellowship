from quantity_measurement.main.length import LengthData
from quantity_measurement.main.measurement_units import MeasurementUnit
from quantity_measurement.main.measurement_exception import MeasurementError


class TestMeasurement:
	def test_for_given_two_measurements_when_added_should_return_added_value(self):
		measurement1 = LengthData(MeasurementUnit.INCH, 1)
		measurement2 = LengthData(MeasurementUnit.YARD, 1)
		expected_value = LengthData(MeasurementUnit.INCH, 37)
		calculated_value = measurement1.__add__(measurement2)
		assert calculated_value.equals(expected_value)

	def test_for_given_two_measurements_of_different_type_when_added_should_throw_exception(self):
		try:
			measurement1 = LengthData(MeasurementUnit.INCH, 1)
			measurement2 = 2
			measurement1.__add__(measurement2)
		except MeasurementError as err:
			assert MeasurementError.ExceptionType.INVALID_ADDITION == err .exception_type
