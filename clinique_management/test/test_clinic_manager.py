from ..main.clinic import ClinicManager


class TestClinicManager:
	DOCTORS_DETAILS_FILE_PATH = "DoctorsDetails.json"

	def test_given_doctors_file_when_loaded_should_give_exact_amount_of_data(self):
		clinic_manager = ClinicManager()
		doctors_data = clinic_manager.load_doctors_details(self.DOCTORS_DETAILS_FILE_PATH)
		assert 8 == doctors_data.__len__()
