from quantity_measurement.main.length import LengthData
from quantity_measurement.main.measurement_units import MeasurementUnit


class TestMeasurement:
	def test_for_given_two_measurements_when_added_should_return_added_value(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 36)
		length_data2 = LengthData(MeasurementUnit.YARD, 1)
		expected_value = 72
		calculated_value = length_data1.__add__(length_data2)
		assert expected_value == calculated_value
