class MoodAnalyser:

	def __init__(self, message=""):
		self.message = message

	def analyse_mood(self):
		try:
			if "sad" in self.message.lower():
				return "SAD"
			return "HAPPY"
		except AttributeError:
			return "HAPPY"
