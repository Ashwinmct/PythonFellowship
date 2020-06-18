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

	def test_given_single_feet_value_with_respective_inch_value_when_equals_should_return_true(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 12)
		length_data2 = LengthData(MeasurementUnit.FEET, 1)
		assert length_data1.equals(length_data2)

	def test_given_zero_feet_and_zero_inch_when_equals_should_return_true(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 0)
		length_data2 = LengthData(MeasurementUnit.FEET, 0)
		assert length_data1.equals(length_data2)

	def test_given_feet_data_with_same_inch_value_and_different_unit_when_equalize_should_return_false(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 1)
		length_data2 = LengthData(MeasurementUnit.FEET, 1)
		assert length_data2.equals(length_data1) is False

	def test_given_inch_value_with_respective_feet_value_when_equals_should_return_true(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 12)
		length_data2 = LengthData(MeasurementUnit.FEET, 1)
		assert length_data2.equals(length_data1)

	def test_given_feet_value_with_respective_yard_value_when_equals_should_return_true(self):
		length_data1 = LengthData(MeasurementUnit.FEET, 3)
		length_data2 = LengthData(MeasurementUnit.YARD, 1)
		assert length_data2.equals(length_data1)

	def test_given_single_unit_feet_and_yard_when_equalized_should_return_false(self):
		length_data1 = LengthData(MeasurementUnit.YARD, 1)
		length_data2 = LengthData(MeasurementUnit.FEET, 1)
		assert length_data2.equals(length_data1) is False

	def test_given_single_unit_inch_and_yard_when_equalized_should_return_false(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 1)
		length_data2 = LengthData(MeasurementUnit.FEET, 1)
		assert length_data2.equals(length_data1) is False

	def test_given_yard_value_with_respective_inch_value_when_equals_should_return_true(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 36)
		length_data2 = LengthData(MeasurementUnit.YARD, 1)
		assert length_data2.equals(length_data1)

	def test_given_inch_value_with_respective_yard_value_when_equals_should_return_true(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 36)
		length_data2 = LengthData(MeasurementUnit.YARD, 1)
		assert length_data1.equals(length_data2)

	def test_given_yard_value_with_respective_feet_value_when_equals_should_return_true(self):
		length_data1 = LengthData(MeasurementUnit.FEET, 3)
		length_data2 = LengthData(MeasurementUnit.YARD, 1)
		assert length_data2.equals(length_data1)

	def test_given_length_in_centimeter_and_respective_length_in_inches_when_equals_should_return_true(self):
		length_data1 = LengthData(MeasurementUnit.INCH, 2)
		length_data2 = LengthData(MeasurementUnit.CENTIMETER, 5)
		assert length_data2.equals(length_data1)
