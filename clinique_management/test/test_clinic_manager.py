from clinique_management.main.clinic_manager import ClinicManager


class TestClinicManager:
	def test_given_doctor_name_when_searched_if_existed_should_return_true(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_doctor_by_name("Ashwin")

	def test_given_doctor_name_when_searched_if_not_existed_should_return_false(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_doctor_by_name("win") is False

