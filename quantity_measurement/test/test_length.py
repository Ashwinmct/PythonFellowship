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

	def test_given_lengths_in_inch_when_added_should_return_added_length_in_inches(self):
		length1 = LengthData(MeasurementUnit.INCH, 2)
		length2 = LengthData(MeasurementUnit.INCH, 2)
		expected_length_in_inch = LengthData(MeasurementUnit.INCH, 4)
		calculated_length_in_inch = length1.__add__(length2)
		assert expected_length_in_inch.equals(calculated_length_in_inch)

	def test_given_lengths_in_inch_and_feet_when_added_should_return_added_length_in_inches(self):
		length1 = LengthData(MeasurementUnit.FEET, 1)
		length2 = LengthData(MeasurementUnit.INCH, 2)
		expected_length_in_inch = LengthData(MeasurementUnit.INCH, 14)
		calculated_length_in_inch = length1.__add__(length2)
		assert expected_length_in_inch.equals(calculated_length_in_inch)

	def test_given_lengths_in_feet_when_added_should_return_added_length_in_inches(self):
		length1 = LengthData(MeasurementUnit.FEET, 1)
		length2 = LengthData(MeasurementUnit.FEET, 1)
		expected_length_in_inch = LengthData(MeasurementUnit.INCH, 24)
		calculated_length_in_inch = length1.__add__(length2)
		assert expected_length_in_inch.equals(calculated_length_in_inch)

	def test_given_lengths_in_inch_and_centimeter_when_added_should_return_added_length_in_inches(self):
		length1 = LengthData(MeasurementUnit.INCH, 2)
		length2 = LengthData(MeasurementUnit.CENTIMETER, 2.5)
		expected_length_in_inch = LengthData(MeasurementUnit.INCH, 3)
		calculated_length_in_inch = length1.__add__(length2)
		assert expected_length_in_inch.equals(calculated_length_in_inch)
