from ..main.clinic_manager import ClinicManager


class TestClinicManager:
	DOCTORS_DETAILS_FILE_PATH = "DoctorsDetails.json"
	PATIENT_DETAILS_FILE_PATH = "PatientsDetails.json"

	def test_given_doctors_details_file_when_loaded_should_give_exact_amount_of_data(self):
		clinic_manager = ClinicManager()
		expected_count = 8
		doctors_data_count = clinic_manager.load_details(self.DOCTORS_DETAILS_FILE_PATH).__len__()
		assert expected_count == doctors_data_count

	def test_given_patient_details_file_when_loaded_should_give_exact_amount_of_data(self):
		clinic_manager = ClinicManager()
		expected_count = 5
		patient_data = clinic_manager.load_details(self.PATIENT_DETAILS_FILE_PATH).__len__()
		assert expected_count == patient_data
