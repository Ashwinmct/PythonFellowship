from ..main.mass import MassData
from ..main.measurement_units import MeasurementUnit
from ..main.measurement_exception import MeasurementError


class TestMass:
	def test_given_mass_data_with_same_value_and_unit_when_equalised_should_return_true(self):
		mass1 = MassData(MeasurementUnit.KILO_GRAM, 1)
		mass2 = MassData(MeasurementUnit.KILO_GRAM, 1)
		assert mass1.equals(mass2)

	def test_given_mass_data_with_same_value_and_different_unit_when_equalised_should_return_false(self):
		mass1 = MassData(MeasurementUnit.KILO_GRAM, 1)
		mass2 = MassData(MeasurementUnit.GRAM, 1)
		assert mass1.equals(mass2) is False

	def test_given_mass_data_with_zero_value_and_different_unit_when_equalised_should_return_true(self):
		mass1 = MassData(MeasurementUnit.KILO_GRAM, 0)
		mass2 = MassData(MeasurementUnit.GRAM, 0)
		assert mass1.equals(mass2)

	def test_given_mass_data_with_different_value_and_same_unit_when_equalised_should_return_false(self):
		mass1 = MassData(MeasurementUnit.KILO_GRAM, 10)
		mass2 = MassData(MeasurementUnit.KILO_GRAM, 1)
		assert mass1.equals(mass2) is False

	def test_given_mass_data_with_same_reference_when_equalised_should_return_true(self):
		mass1 = MassData(MeasurementUnit.KILO_GRAM, 10)
		mass2 = mass1
		assert mass1.equals(mass2)

	def test_given_mass_data_with_invalid_unit_should_raise_exception(self):
		try:
			MassData(MeasurementUnit.LITRE, 1)
		except MeasurementError as err:
			assert MeasurementError.ExceptionType.INVALID_UNIT == err.exception_type

	def test_given_mass_data_in_kg_and_g_unit_when_equalised_should_return_true(self):
		mass1 = MassData(MeasurementUnit.KILO_GRAM, 1)
		mass2 = MassData(MeasurementUnit.GRAM, 1000)
		assert mass1.equals(mass2)

	def test_given_mass_data_in_kg_and_tonne_unit_when_equalised_should_return_true(self):
		mass1 = MassData(MeasurementUnit.KILO_GRAM, 1000)
		mass2 = MassData(MeasurementUnit.TONNE, 1)
		assert mass1.equals(mass2)
