from mood_analyser.main.mood_analysis_exception import MoodAnalysisException


class MoodAnalyser:

	def __init__(self, message=""):
		self.message = message

	def analyse_mood(self):
		try:
			if len(self.message) == 0:
				raise MoodAnalysisException(MoodAnalysisException.ExceptionType.EMPTY)
			return "SAD" if "sad" in self.message.lower() else "HAPPY"
		except TypeError:
			raise MoodAnalysisException(MoodAnalysisException.ExceptionType.NULL)
