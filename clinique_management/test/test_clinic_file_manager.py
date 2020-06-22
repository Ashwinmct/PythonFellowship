from clinique_management.main.clinic_file_manager import ClinicFileManager
from clinique_management.main.person_type import PersonType


class TestClinicFileManager:
	DOCTORS_DETAILS_FILE_PATH = "DoctorsDetails.json"
	PATIENT_DETAILS_FILE_PATH = "PatientsDetails.json"

	def test_given_doctors_details_file_when_loaded_should_give_exact_amount_of_data(self):
		clinic_manager = ClinicFileManager()
		expected_count = 3
		doctors_data_count = clinic_manager.open(PersonType.DOCTOR, self.DOCTORS_DETAILS_FILE_PATH).__len__()
		assert expected_count == doctors_data_count

	def test_given_patient_details_file_when_loaded_should_give_exact_amount_of_data(self):
		clinic_manager = ClinicFileManager()
		expected_count = 5
		patient_data = clinic_manager.open(PersonType.PATIENT, self.PATIENT_DETAILS_FILE_PATH).__len__()
		assert expected_count == patient_data
