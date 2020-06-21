from clinique_management.main.clinic_file_manager import ClinicFileManager


class ClinicManager:

	def load_details(self, file_path):
		file_loader = ClinicFileManager()
		file_data = file_loader.open(file_path)
		return file_data
