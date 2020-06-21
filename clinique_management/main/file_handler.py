import json
from .doctor import Doctor


class ClinicFileHandler:

	def convert_to_list(self,json_string):
		doctor_list = []
		for doc in json_string:
			doctor_list.append(self.store_to_object(doc))
		return doctor_list

	def open(self, file_path):
		with open(file_path) as f:
			return self.convert_to_list(json.load(f))

	def store_to_object(self, doc):
		return Doctor(doc["Name"], doc["ID"], doc["Specialisation"], doc["Availability"])
