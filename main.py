from sigma import SigmaController

# main loop
sigma = SigmaController()
sigma.printUserSpeech = True
sigma.printResponse = True
sigma.printStatus = True

def main():
	while True:
		sigma.communicate()
main()