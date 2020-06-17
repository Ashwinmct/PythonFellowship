from quantity_measurement.main.Length_data import LengthData


class TestLengthData:
	def test_given_length_data_with_same_value_when_equalize_should_return_true(self):
		length_data1 = LengthData(1)
		length_data2 = LengthData(1)
		assert length_data1.equals(length_data2)

	def test_given_length_data_with_value_and_none_when_equalize_should_return_false(self):
		length_data1 = LengthData(1)
		length_data2 = None
		assert length_data1.equals(length_data2) is False

	def test_given_length_data_with_same_reference_when_equalize_should_return_true(self):
		length_data1 = LengthData(1)
		length_data2 = length_data1
		assert length_data1.equals(length_data2)

	def test_given_length_data_with_different_when_equalize_should_return_false(self):
		length_data1 = LengthData(1)
		length_data2 = LengthData(10)
		assert length_data1.equals(length_data2) is False

