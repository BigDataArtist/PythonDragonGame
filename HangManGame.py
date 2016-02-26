import random
HANGMANPICS = ['''

  +---+
  |   |
	  |
	  |
	  |
	  |
=========''', '''

  +---+
  |   |
  O   |
	  |
	  |
	  |
=========''', '''

  +---+
  |   |
  O   |
  |   |
	  |
	  |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
	  |
	  |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
	  |
	  |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
	  |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
	  |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra coug coyote  crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizardllama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ra rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):

	wordIndex = random.randint(0,len(wordList)-1)

	return wordList[wordIndex]

def displayBoard(HANGMANPICS,Correctletters,missedletters,secretWord):

	print(HANGMANPICS[len(missedletters)])

	print()

	print('Missed letters:')
	for letters in missedletters:
		print(letters)
	print()

	blanks =' '*len(secretWord)

	for i in range(len(secretWord)):
         if secretWord[i] in Correctletters:
			blanks = blanks[:i]+secretWord[i]+blanks[i+1:]

	for letters in blanks:

		print(letters)
	print()

def getGuess(alreadyGuessed):

	while True:
		print('Guess a letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) !=1:
			print(' Enter the single letter')
		elif guess in alreadyGuessed:
			print(' you have already choosed that letter , choose again')
		elif guess not in 'avshavdhavdjhdjhabdhdbwhcb':
			print(' Please enter the letter')
		else:
			return guess

def playAgain():

	print(' do you want to play again(Yes od No)?')
	return input().lower().startswith('y')


print(' H A N G M A N')

missedletters =''
Correctletters=''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	displayBoard(HANGMANPICS,missedletters,Correctletters,secretWord)


	guess =getGuess(missedletters+Correctletters)

	if guess in secretWord:
		Correctletters=Correctletters+guess

		foundAllLetters = True

		for i in range(len(secretWord)):
		    if secretWord[i] not in Correctletters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print(' yes the secretWord is ',secretWord,'you have won')

			gameIsDone = True
	else:
			missedletters = missedletters + guess

			if len(missedletters) == len(HANGMANPICS)-1:
				displayBoard(HANGMANPICS,missedletters,Correctletters,secretWord)

				print(' you have run out of guesses',len(missedletters),'missed guesses',len(Correctletters),'correct guesses the word was',secretWord,)

				gameIsDone = True

	if gameIsDone:
		if playAgain():
			missedletters=''
			Correctletters=''
			gameIsDone = False
			secretWord = getRandomWord(words)
		else:
			break



