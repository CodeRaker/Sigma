from sigma import SigmaController
from gui import TerminalController

#development

# main loop
sigma = SigmaController()
sigma.printUserSpeech = True
sigma.printResponse = True
sigma.printStatus = True

terminal = TerminalController()
terminal.terminalImageID = "C:\\Users\\Peter\\Documents\\pythoncode\\sigma\\pyautogui-images\\hyper-corner.jpg"
terminal.terminalExecutablePath = "C:\\Users\\Peter\\AppData\\Local\\hyper\\Hyper.exe"

def main():
	#while True:
		#sigma.communicate()
		#action = sigma.sigma.listen(True)
		#print("action: "+action)
	terminal.typeInTerminal("ping heimdal.hammerheim.net")

main()