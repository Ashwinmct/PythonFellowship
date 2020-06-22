import json
from clinique_management.main.person_type import PersonType
from .patient import Patient
from .doctor import Doctor


class ClinicFileManager:

	def convert_to_list(self, person_type, json_string):
		person_details = []
		for person in json_string:
			person_details.append(self.store_to_object(person_type, person))
		return person_details

	def open(self, person_type, file_path):
		with open(file_path) as f:
			return self.convert_to_list(person_type, json.load(f))

	def store_to_object(self, person_type, person):
		if person_type == PersonType.DOCTOR:
			return Doctor(person["Name"], person["ID"], person["Specialisation"], person["Availability"])
		return Patient(person["Name"], person["ID"], person["MobileNumber"], person["Age"])
