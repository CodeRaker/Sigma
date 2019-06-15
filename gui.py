import pyautogui
import os
import time

class TerminalController:
	def __init__(self):
		self.typingSpeed = 0.05
		self.terminalOpened = False
		self.terminalActive = False
		self.terminalImageID = ""
		self.terminalExecutablePath = ""

	def typeInTerminal(self, command):
		if not self.terminalOpened:
			os.system(self.terminalExecutablePath)
			time.sleep(1)
			self.terminalOpened = True

		if not self.terminalActive:
			try:
				terminal_x, terminal_y = pyautogui.locateCenterOnScreen(self.terminalImageID, confidence=.5)
				pyautogui.click(terminal_x, terminal_y + 20)
				self.terminalActive = True

			except Exception as e:
				self.terminalActive = False
			
		if self.terminalOpened and self.terminalActive:
			pyautogui.typewrite(command, interval=self.typingSpeed)
			pyautogui.press(['enter'])
			self.terminalActive = False