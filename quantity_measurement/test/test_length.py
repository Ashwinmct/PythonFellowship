from quantity_measurement.main.length import LengthData
from quantity_measurement.main.measurement_units import MeasurementUnit


class TestLengthData:
	def test_given_length_data_with_same_value_and_unit_when_equalize_should_return_true(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 1)
		length_data2 = LengthData(MeasurementUnit.INCH, 1)
		assert length_data1.equals(length_data2)

	def test_given_length_data_with_value_and_none_when_equalize_should_return_false(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 1)
		length_data2 = None
		assert length_data1.equals(length_data2) is False

	def test_given_length_data_with_same_reference_when_equalize_should_return_true(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 1)
		length_data2 = length_data1
		assert length_data1.equals(length_data2)

	def test_given_length_data_with_different_value_and_same_unit_when_equalize_should_return_false(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 1)
		length_data2 = LengthData(MeasurementUnit.INCH, 10)
		assert length_data1.equals(length_data2) is False

	def test_given_length_data_with_same_value_and_different_unit_when_equalize_should_return_false(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 1)
		length_data2 = LengthData(MeasurementUnit.FEET, 1)
		assert length_data1.equals(length_data2) is False
