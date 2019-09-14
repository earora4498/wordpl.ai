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

	#read words from file and organize them into a map
	file = open("5000words.txt", "r")
	text = file.read()
	myList = text.split()
	first500 = myList[0:499]
	words = set(first500)

	#get a phrase from the user
	phraseInput = raw_input("Enter a phrase: ")
	phrase = phraseInput.split()

	#check if every word in phrase is also in the map
	for word in phrase:
		if (word not in words):
			print("Oh no! The word \'" + word + "\' is not in the 500 most frequent words!")
			sys.exit(0)

	print("That's a valid phrase!")
elif gameChoice == '2':
#Being Extra
	print("TODO")
elif gameChoice == '3':
#Up/Down
	print("TODO")