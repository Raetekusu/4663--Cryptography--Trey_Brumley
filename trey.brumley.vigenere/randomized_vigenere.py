######################################
# Name: Trey Brumley
# Class: CMPS 4663 Cryptography
# Date: 28 July 2015
# Program 2 - Vigenere Cipher
######################################

import random
from pprint import pprint
seed = 12001907 # seed is "MATH"

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~""" # Character Set for the cipher
size = len(SYMBOLS) # Length and width of the tableau
ekey = [] # The empty key to be added to during encryption (Encryption Key)
dkey = [] # The empty key to be added to during decryption (Decryption Key)

# "Translates" a keyword from a seed
# Code provided on Program page on GitHub
def keywordFromSeed(seed):
    Letters = []

    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(Letters)
	
# builds Vigenere tableau from the seed and the character set
# Code used in class on Monday
def buildVigenere(chars, seed):
    random.seed(seed)
    vigenere = [[0 for i in range(size)] for i in range(size)]
    chars = list(chars)
    random.shuffle(chars)
    chars =''.join(chars)

    for sym in chars:
        random.seed(seed)
        myList =[]
        for i in range(size):
            r = random.randrange(size)
            if r not in myList:
                myList.append(r)
            else:
                while(r in myList):
                    r = random.randrange(size)
                myList.append(r)
            while(vigenere[i][r] != 0):
                r = (r + 1) % size
            vigenere[i][r] = sym
    return vigenere

# Encrypts the plaintext using a keyword and a seed
def encrypt(plain_text_message,keyword,seed):

	# Builds keyword and cipher from seed.
	key = keywordFromSeed(seed)
	cipher = buildVigenere(SYMBOLS,seed)
	C = 0
	
	# Loops through letter by letter to find the correct new value for decryption
	for i in range(len(plain_text_message)):
		
		# Loops through to find X and Y values to decrypt
		for j in range(size):
			if cipher[j][0] == plain_text_message[i]:
				C = j;
		for k in range(size):
			if cipher[C][k] == plain_text_message[i]:
				C = k
		
		# Appends the new character to the key	
		ekey.append(cipher[0][C])
	
	# Creates the string and adds the characters in order, then returns
	encrypted = ''.join(str(e) for e in ekey)
	return encrypted
	
# Decrypts ciphertext using the keyword and seed
def decrypt(cipher_text_message,keyword,seed):

	# Builds keyword and cipher from seed
	key = keywordFromSeed(seed)
	cipher = buildVigenere(SYMBOLS,seed)
	C = 0
	C2 = 0
	
	# Loops through letter by letter to find the correct new value for encryption
	for i in range(len(cipher_text_message)):
		
		# Loops through to find X and Y values to encrypt
		for j in range(size):
			if cipher[0][j] == cipher_text_message[i]:
				C = j
		for k in range(size):
			if cipher[C][0] == cipher_text_message[i]:
				C2 = k
						
		# Appends the new character to the key					
		dkey.append(cipher[C2][C])
	
	# Creates the string and adds the characters in order, then returns
	decrypted = ''.join(str(d) for d in dkey)
	return decrypted