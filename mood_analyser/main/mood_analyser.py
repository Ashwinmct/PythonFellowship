class MoodAnalyser:
	def analyse_mood(self, mood):
		if "sad" in mood.lower():
			return "SAD"
		return "HAPPY"