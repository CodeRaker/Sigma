# SpeechToText
import speech_recognition as sr

# TextToSpeech
import pyttsx3

# ChatBrain
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


# The ear
class SpeechToText:
	def __init__(self):
		self.voiceController = sr.Recognizer()

	def listen(self):
		with sr.Microphone() as source:
		    self.voiceInput = self.voiceController.listen(source)

		try:
			self.voiceTranslatedToText = self.voiceController.recognize_google(self.voiceInput)
			return self.voiceTranslatedToText
		except sr.UnknownValueError:
			return "Error: No matches"
		except sr.RequestError as e:
			return "Error: " + e


# The mouth
class TextToSpeech:
	def __init__(self):
		self.engine = pyttsx3.init()

	def speak(self, words):
		self.engine.say(words)
		self.engine.runAndWait()


# The brain
class ChatBrain:
	def __init__(self, chatBotName, chatBotWordList):
		self.chatBot = ChatBot(chatBotName)
		self.chatBot.storage.drop()
		self.trainer = ListTrainer(self.chatBot)
		self.trainer.train(chatBotWordList)

	def calculateResponse(self, inputText):
		return str(self.chatBot.get_response(inputText))