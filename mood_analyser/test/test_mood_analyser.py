import pytest
from mood_analyser.main.mood_analyser import MoodAnalyser
from mood_analyser.main.mood_analysis_exception import MoodAnalysisException


class TestMoodAnalyser:

	def test_given_string_with_the_word_Sad_when_analysed_should_return_SAD(self):
		mood_analyser = MoodAnalyser("I am in Sad Mood")
		expected_mood = 'SAD'
		calculated_mood = mood_analyser.analyse_mood()
		assert expected_mood == calculated_mood

	def test_given_string_without_the_word_Sad_when_analysed_should_return_HAPPY(self):
		mood_analyser = MoodAnalyser("I am in Happy Mood")
		expected_mood = 'HAPPY'
		calculated_mood = mood_analyser.analyse_mood()
		assert expected_mood == calculated_mood

	def test_given_empty_string_when_analysed_should_raise_exception(self):
		try:
			MoodAnalyser().analyse_mood()
		except MoodAnalysisException as err:
			assert MoodAnalysisException.ExceptionType.EMPTY == err.exception_type

	def test_given_None_value_when_analysed_should_raise_exception(self):
		try:
			mood_analyser = MoodAnalyser(None)
			mood_analyser.analyse_mood()
		except MoodAnalysisException as err:
			assert MoodAnalysisException.ExceptionType.NULL == err.exception_type