from clinique_management.main.file_handler import ClinicFileHandler


class ClinicManager:

	def load_doctors_details(self, doctors_details_file_path):
		file_loader = ClinicFileHandler()
		file_data = file_loader.open(doctors_details_file_path)
		return file_data
