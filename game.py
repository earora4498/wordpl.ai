import sys
import random

gameChoice = raw_input("Choose a game!\n\nType '1' for Taboo\nType '2' for Being Extra\nType '3' for Up/Down\n")


if gameChoice == '1':
#Taboo

	file = open("tabooWords.txt", "r")
	text = file.read()
	myList = text.split()
	taboo = random.choice(myList)

	print("Your taboo phrase is: " + taboo)

	file = open("5000words.txt", "r")
	text = file.read()
	myList = text.split()

	first1000 = myList[0:999]
	words = set(first1000)

	#get a phrase from the user
	phraseInput = raw_input("Enter a phrase: ")
	phrase = phraseInput.split()

	#check if every word in phrase is also in the map
	for word in phrase:
		if (word not in words):
			print("Oh no! The word \'" + word + "\' is not in the 1000 most frequent words!")
			sys.exit(0)

	print("That's a valid phrase!")
elif gameChoice == '2':
#Being Extra

	file = open("tabooWords.txt", "r")
	text = file.read()
	myList = text.split()
	taboo = random.choice(myList)

	print("Your taboo phrase is: " + taboo)

	file = open("30000words.txt", "r")
	text = file.read()
	myList = text.split()

	words = set(myList)

	phraseInput = raw_input("Enter a phrase: ")
	phrase = phraseInput.split()

	for word in phrase:
		if (word in words):
			print(myList.index(word))


elif gameChoice == '3':
#Up/Down
	
	file = open("30000words.txt", "r")
	text = file.read()
	myList = text.split()
	words = set(myList)

	currentWord = random.choice(myList)

	done = False

	while (not done):
		currValue = myList.index(currentWord)
		direction = bool(random.getrandbits(1))
		directionWord = "more" if direction else "less"
		print("The current word is " + currentWord)

		nextWord = raw_input("Say a word that is used " + directionWord + " frequently than the current word!\n")

		if (nextWord in words):
			value = myList.index(nextWord)
			if (direction):
				if (value > currValue):
					done = True
					print("Wrong!")
				else:
					currentWord = nextWord
					currValue = value
			else:
				if (value < currValue):
					done = True
					print("Wrong!")
				else:
					currentWord = nextWord
					currValue = value
		else:
			print("That word isn't in our dictionary - sorry!")
