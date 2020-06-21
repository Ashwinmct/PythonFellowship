import json
from .patient import Patient
from .doctor import Doctor


class ClinicFileManager:

	def convert_to_list(self,json_string):
		person_list = []
		for person in json_string:
			person_list.append(self.store_to_object(person))
		return person_list

	def open(self, file_path):
		with open(file_path) as f:
			return self.convert_to_list(json.load(f))

	def store_to_object(self, person):
		if '__type__' in person and person["__type__"] == "Doctor":
			return Doctor(person["Name"], person["ID"], person["Specialisation"], person["Availability"])
		if '__type__' in person and person["__type__"] == "Patient":
			return Patient(person["Name"], person["ID"], person["Specialisation"], person["Availability"])
