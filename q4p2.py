# Filename: q4p2.py
# Author: William Lohmann, 000762544
# Course: ITSC203
# Details: Similair to q4p1, but with modified password length range and a function to work backwards to find a passcode from a hash


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


############################### Reverse Hash Lookup ################################


garysHash = "0c607ee94ea63a6793c9569d7168c48761e65ab3fb4d296454484de4b0cef9318eb110d9fb11a8bb8781fec614f714fd9f9067c9e7ad026786702e1359681ada"
hashFind = []

for phrase in passList:
	hashOut = hashlib.sha512(phrase.encode()).hexdigest()
	hashFind.append(hashOut)
	
count = 0
for hashDigest in hashFind:
	if hashDigest == garysHash:
		print(passList[count])
	count += 1
	

	



