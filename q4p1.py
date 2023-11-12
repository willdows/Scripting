# Filename: q4p1.py
# Author: William Lohmann, 000762544
# Course: ITSC203
# Details: This program generates 512 passphrases using two .txt file input, and prints ...
# ...the results as well as their SHA512 hashed digests


import hashlib


############################## Getting passphrase length ##############################

 
passLen = 0
while passLen < 16 or passLen > 22:
	passLen = int(input("Please enter the length of your desired passphrase as an integer between 16 and 22: "))
	if passLen < 16 or passLen > 22:
		print("\nOut of bounds!\n")


################################# Reading text files #################################


tempList = open("first.txt").readlines()
firstList = [line.strip() for line in tempList] # Removing whitespace & newlines

tempList = [""] # Clearing for peace of mind

tempList = open("second.txt").readlines()
secondList = [line.strip() for line in tempList]


################################# Replacement Cipher #################################


repCipher = {'o':'0', 'l': '!', 's': '5', 'e':'3', 'a': '@', 'i': '1'} # Replacement Cipher

def substitution_cipher(subDict, inList):
	swapped = []
	for word in inList:
		new_word = ""
		for char in word:
			if char in subDict:
				new_word += subDict[char]
			else:
				new_word += char
		swapped.append(new_word)
	
	return swapped
	
firstSwap = substitution_cipher(repCipher,firstList)
secondSwap = substitution_cipher(repCipher,secondList)

############################### Generating Passphrases ###############################


firstGen = firstSwap # First Generated list of words from first.txt
secondGen = firstSwap # Second Generated list of words from first.txt
thirdGen = secondSwap # Third generated list of words from second.txt
passList = [] # For storing the calculated passphrases

while len(passList) < 512:

	for word in firstGen:
		for second_word in secondGen:
			passphrase = ""
			passphrase += word
			passphrase += second_word
	
		if len(passphrase) == passLen:
			passList.append(passphrase)
		
		elif len(passphrase) < passLen:
			for third_word in thirdGen:
				if (len(third_word) + len(passphrase)) == passLen:
					passphrase += third_word
					passList.append(passphrase)
				
		
################################# Genrating Hashes #################################

	
def sha512_hash(inputList):
	with open('rainbow.txt','w') as outFile:
		for phrase in inputList:
			digest = hashlib.sha512(phrase.encode()).hexdigest()
			outFile.write(f"{phrase} - {digest}\n")
	
sha512_hash(passList)

