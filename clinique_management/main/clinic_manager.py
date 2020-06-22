import enum

from clinique_management.main.clinic_file_manager import ClinicFileManager
from clinique_management.main.person_type import PersonType


class ClinicManager:

	class Option(enum.Enum):
		NAME = 'name'
		ID = 'id'
		SPECIALISATION = 'specialisation'
		AGE = 'age'
		MOBILE_NUMBER = 'mobile_number'

	DOCTORS_DETAILS_FILE_PATH = "DoctorsDetails.json"
	PATIENT_DETAILS_FILE_PATH = "PatientsDetails.json"

	def __init__(self):
		self.doctor_details_list = self.load_details(PersonType.DOCTOR, self.DOCTORS_DETAILS_FILE_PATH)
		self.patient_details_list = self.load_details(PersonType.PATIENT, self.PATIENT_DETAILS_FILE_PATH)

	def load_details(self,person_type,  file_path):
		file_loader = ClinicFileManager()
		file_data = file_loader.open(person_type, file_path)
		return file_data

	def search_by(self, option, value):
		for doctor in self.doctor_details_list:
			if doctor.__getattribute__(option.value) == value:
				return True
		return False
