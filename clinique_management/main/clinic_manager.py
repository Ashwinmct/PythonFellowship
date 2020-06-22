import enum
from clinique_management.main.clinic_file_manager import ClinicFileManager
from clinique_management.main.clinic_management_exception import ClinicManagementError
from clinique_management.main.person_type import PersonType


class ClinicManager:
	MAXIMUM_PATIENT_PER_AVAILABILITY = 5
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

	def load_details(self, person_type,  file_path):
		file_loader = ClinicFileManager()
		file_data = file_loader.open(person_type, file_path)
		return file_data

	def search_by(self, person_type, option, value):
		person_list = self.__get_details_of(person_type)
		for person in person_list:
			if person.__getattribute__(option.value) == value:
				return True
		return False

	def __get_details_of(self, person_type):
		return self.doctor_details_list if person_type == PersonType.DOCTOR else self.patient_details_list

	def fix_appointment(self, doctor_name, patient_name):
		doctor = self._get_person_details(PersonType.DOCTOR,doctor_name)
		patient = self._get_person_details(PersonType.PATIENT, patient_name)
		if doctor.appointment_details.__len__() < self.MAXIMUM_PATIENT_PER_AVAILABILITY:
			doctor.appointment_details.append(patient)
			return "appointment fixed"
		return "appoint not fixed "

	def _get_person_details(self, person_type, name):
		person_list = self.__get_details_of(person_type)
		for person in person_list:
			if person.name == name:
				return person
		raise ClinicManagementError(ClinicManagementError.ExceptionType.NOT_FOUND)
