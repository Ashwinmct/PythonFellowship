class MoodAnalyser:

	def __init__(self, message):
		self.message = message

	def analyse_mood(self):
		if "sad" in self.message.lower():
			return "SAD"
		return "HAPPY"
