import sys

#read words from file and organize them into a map
file = open("5000words.txt", "r")
text = file.read()
myList = text.split()
words = set(myList)

#get a phrase from the user
input = raw_input("Enter a phrase: ")
phrase = input.split()

#check if every word in phrase is also in the map
for word in phrase:
	if (word not in words):
		print("Oh no! The word \'" + word + "\' is not in the 5000 most frequent words!")
		sys.exit(0)

print("That's a valid phrase!")
