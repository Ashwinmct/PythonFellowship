import pytest
from mood_analyser.main.mood_analyser import MoodAnalyser


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

	def test_given_empty_string_when_analysed_should_return_HAPPY(self):
		mood_analyser = MoodAnalyser()
		expected_mood = 'HAPPY'
		calculated_mood = mood_analyser.analyse_mood()
		assert expected_mood == calculated_mood