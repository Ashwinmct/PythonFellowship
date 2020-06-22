from clinique_management.main.clinic_manager import ClinicManager


class TestClinicManager:
	def test_given_doctor_name_when_searched_if_existed_should_return_true(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(ClinicManager.Option.NAME, "Ashwin")

	def test_given_doctor_name_when_searched_if_not_existed_should_return_false(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(ClinicManager.Option.NAME, "Ashwin") is False

	def test_given_doctor_id_when_searched_by_if_existed_should_return_true(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(ClinicManager.Option.ID, "DOC001")

	def test_given_doctor_id_when_searched_by_if_existed_should_return_false(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(ClinicManager.Option.ID, "1") is False

	def test_given_doctor_specialisation_when_searched_by_if_existed_should_return_true(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(ClinicManager.Option.SPECIALISATION, "Pediatrecian")
