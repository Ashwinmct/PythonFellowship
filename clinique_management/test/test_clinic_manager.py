from clinique_management.main.clinic_manager import ClinicManager
from clinique_management.main.person_type import PersonType


class TestClinicManager:
	def test_given_doctor_name_when_searched_if_existed_should_return_true(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(PersonType.DOCTOR, ClinicManager.Option.NAME, "Ashwin")

	def test_given_doctor_name_when_searched_if_not_existed_should_return_false(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(PersonType.DOCTOR, ClinicManager.Option.NAME, "win") is False

	def test_given_doctor_id_when_searched_by_if_existed_should_return_true(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(PersonType.DOCTOR, ClinicManager.Option.ID, "DOC001")

	def test_given_doctor_id_when_searched_by_if_existed_should_return_false(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(PersonType.DOCTOR, ClinicManager.Option.ID, "1") is False

	def test_given_doctor_specialisation_when_searched_by_if_existed_should_return_true(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(PersonType.DOCTOR, ClinicManager.Option.SPECIALISATION, "Pediatrecian")

	def test_given_patient_name_when_searched_by_if_existed_should_return_true(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(PersonType.PATIENT, ClinicManager.Option.NAME, "Sarath")

	def test_given_patient_mobile_number_when_searched_by_if_existed_should_return_true(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(PersonType.PATIENT, ClinicManager.Option.MOBILE_NUMBER, 9441234567)

	def test_given_patient_id_when_searched_by_if_existed_should_return_true(self):
		clinic_manager = ClinicManager()
		assert clinic_manager.search_by(PersonType.PATIENT, ClinicManager.Option.ID, "P001")

	def test_given_patient_should_get_appointment_from_the_doctor(self):
		clinic_manager = ClinicManager()
		expected_message = "appointment fixed"
		message_got = clinic_manager.fix_appointment("Ashwin", "Sarath")
		assert expected_message == message_got
