from clinique_management.main.file_handler import ClinicFileHandler


class ClinicManager:

	def load_details(self, file_path):
		file_loader = ClinicFileHandler()
		file_data = file_loader.open(file_path)
		return file_data
