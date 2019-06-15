from humanInteraction import SpeechToText, TextToSpeech, ChatBrain

class Sigma:

	"""Sigma is the awesome intelligence of my imagination"""

	def __init__(self):
		with open("chatBotWordList.txt", "r") as f:
			chatBotWordList = f.readlines()
		self.brain = ChatBrain("Sigma", chatBotWordList)
		self.ear = SpeechToText()
		self.mouth = TextToSpeech()
		self.reponse = ""

	def listen(self, verbose):
		self.voiceInput = self.ear.listen()
		if verbose:
			print("User: "+self.voiceInput)
		return self.voiceInput

	def interpret(self, verbose):
		self.response = self.brain.calculateResponse(self.voiceInput)
		if verbose:
			print("Sigma: "+self.response)
		return self.response

	def speak(self):
		self.mouth.speak(self.response)
		return self.response

class SigmaController:

	"""The controller provides a more user friendly experience, by combining the Sigma functionality into a meaning interactive experience"""

	def __init__(self):
		self.sigma = Sigma()
		self.printUserSpeech = False
		self.printResponse = False
		self.printStatus = False

	def communicate(self):
		if self.printStatus:
			print("Listening ...")
		self.sigma.listen(self.printUserSpeech)
		self.sigma.interpret(self.printResponse)
		self.sigma.speak()