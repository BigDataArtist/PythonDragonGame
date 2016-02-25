
import random 
import time

def displayIntro():
	print(" your are in the lanf full of dragons")
	print(" The dragons will eat you if you choose wrong cave")
	print()

def chooseCave():
	cave = ''
	while cave !=1 and cave !=2:
		print("Enter the cave number you want to Enter(1 or 2)")
		cave = input()

	return cave

def checkCave(chosenCave):
	print(' you approach the cave')
	time.sleep(2)
	print(' Its darka and spoooky')
	time.sleep(2)
	print(" A large dragon jumps in front of you! He opens his jaws")

	print()
	time.sleep(2)

	friendlyCave = random.randint(1,2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasures')
	else: 
		print('Gobbles you down in one bite')

playAgain = 'yes'
while playAgain =='yes' or playAgain =='y':

	displayIntro()

	caveNumber = chooseCave()

	checkCave(caveNumber)

	print('Do you want to play again? (yes or no)')

	playAgain = input()
