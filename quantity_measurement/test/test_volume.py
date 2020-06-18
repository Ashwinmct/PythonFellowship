from ..main.volume import VolumeData
from ..main.measurement_units import MeasurementUnit

class TestVolume:
	def test_given_volume_data_with_same_unit_and_value_when_equalised_should_return_true(self):
		volume1 = VolumeData(MeasurementUnit.LITRE, 1)
		volume2 = VolumeData(MeasurementUnit.LITRE, 1)
		assert volume1.equals(volume2)

	def test_given_volume_data_with_same_unit_and_differnt_value_when_equalised_should_return_false(self):
		volume1 = VolumeData(MeasurementUnit.LITRE, 10)
		volume2 = VolumeData(MeasurementUnit.LITRE, 1)
		assert volume1.equals(volume2) is False

	def test_given_volume_data_with_different_unit_and_same_value_when_equalised_should_return_false(self):
		volume1 = VolumeData(MeasurementUnit.GALLON, 1)
		volume2 = VolumeData(MeasurementUnit.LITRE, 1)
		assert volume1.equals(volume2) is False

	def test_given_volume_data_with_different_unit_and__zero_value_when_equalised_should_return_true(self):
		volume1 = VolumeData(MeasurementUnit.LITRE, 0)
		volume2 = VolumeData(MeasurementUnit.LITRE, 0)
		assert volume1.equals(volume2)

	def test_given_volume_data_with_same_reference_when_equalised_should_return_true(self):
		volume1 = VolumeData(MeasurementUnit.LITRE, 1)
		volume2 = volume1
		assert volume1.equals(volume2)
