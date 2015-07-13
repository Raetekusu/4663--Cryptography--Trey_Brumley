###############################################
# Name: Trey Brumley
# Class: CMPS 4663 Cryptography
# Date: 13 July 2015
# Program 1 - Playfair Cipher
# Some of starter code was used.
###############################################

import pprint
import re

def generateAlphabet():
    #Create empty alphabet string
    alphabet = ""
    
    #Generate the alphabet
    for i in range(0,26):
        alphabet = alphabet + chr(i+65)
        
    return alphabet


def cleanString(s,options = {'up':1,'reNonAlphaNum':1,'reSpaces':'_','spLetters':'X'}):
    """
    Cleans message by doing the following:
    - up            - uppercase letters
    - spLetters     - split double letters with some char
    - reSpaces      - replace spaces with some char or '' for removing spaces
    - reNonAlphaNum - remove non alpha numeric
    - reDupes       - remove duplicate letters
    @param   string -- the message
    @returns string -- cleaned message
    """
    if 'up' in options:
        s = s.upper()
        
    if 'spLetters' in options:
        #replace 2 occurences of same letter with letter and 'X'
        s = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', s)
        
    if 'reSpaces' in options:
        space = options['reSpaces']
        s = re.sub(r'[\s]', space, s)
    
    if 'reNonAlphaNum' in options:
        s = re.sub(r'[^\w]', '', s)
        
    if 'reDupes' in options:
        s= ''.join(sorted(set(s), key=s.index))
        
    return s

def generateSquare(key):
    """
    Generates a play fair square with a given keyword.
    @param   string   -- the keyword
    @returns nxn list -- 5x5 matrix
    """
    row = 0     #row index for sqaure
    col = 0     #col index for square
    
    #Create empty 5x5 matrix 
    playFair = [[0 for i in range(5)] for i in range(5)]
    
    alphabet = generateAlphabet()
    
    #uppercase key (it meay be read from stdin, so we need to be sure)
    key = cleanString(key,{'up':1,'reSpaces':'','reNonAlphaNum':1,'reDupes':1})
    
    print(key)
    
    #Load keyword into square
    for i in range(len(key)):
        playFair[row][col] = key[i]
        alphabet = alphabet.replace(key[i], "")
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    #Remove "J" from alphabet
    alphabet = alphabet.replace("J", "")
    
    #Load up remainder of playFair matrix with 
    #remaining letters
    for i in range(len(alphabet)):
        playFair[row][col] = alphabet[i]
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    return playFair
	
def encodeMessage(Message, playFair):
	#Removes spaces, numbers, and special characters, converts to ALLCAPS, and splits repeated characters with X
	Message = cleanString(Message,{'up':1,'reSpaces':'','reNonAlphaNum':1,'spLetters':1})
	#Replaces all Js with Is
	Message = Message.replace("J","I")
	
	if len(Message)%2 ==1:
		Message += 'X'
		
	length = 0
	#initialize empty character set
	encoded = ''
	#Loop through, find location of letters for digraph, check relation to each other, and encode how necessary
	while(length<len(message)):
		x1,y1 = findLetter(message[length], playFair) #Finds location of first letter of digraph in cipher
		x2,y2 = findLetter(message[length+1], playFair) #Finds location of second letter of digraph in cipher
		
		#Same row
		if(x1==x2):
			encoded += playFair[x1][(y1+1)%5]
			encoded += playFair[x2][(y2+1)%5]
		#Same column
		elif(y1==y2):
			encoded += playFair[(x1+1)%5][y1]
			encoded += playFair[(x2+1)%5][y2]
		#Forms quadrilateral
		else:
			encoded += playFair[x1][y2]
			encoded += playFair[x2][y1]
			
		length += 2
	return encoded
	
def findLetter(letter, playFair):
	#finds letter in matrix
	row = 0
	col = 0

    	for r in range(5):
            for c in range(5):
                if (playFair[i][j] == letter):
                    row = r
                    col = c
        return row,col
 
def decodeMessage(encoded, playFair):
	length = 0
	#initialize empty character set
	encoded = ''
	#Loop through, find location of letters for digraph, check relation to each other, and encode how necessary
	while(length<len(message)):
		x1,y1 = findLetter(message[length], playFair) #Finds location of first letter of digraph in cipher
		x2,y2 = findLetter(message[length+1], playFair) #Finds location of second letter of digraph in cipher
		
		#Same row
		if(x1==x2):
			encoded += playFair[x1][(y1+4)%5] #Added four to prevent negatives
			encoded += playFair[x2][(y2+4)%5] #Will still read as -1
		#Same column
		elif(y1==y2):
			encoded += playFair[(y1+4)%5][y1]
			encoded += playFair[(y1+4)%5][y2]
		#Forms quadrilateral
		else:
			encoded += playFair[x1][y2]
			encoded += playFair[x2][y1]
			
		length += 2
	return Message
	


###########################################################################

print("Playfair Encryption Tool (P.E.T)")
print("Written By: Trey Brumley")
print("*************************************")
print("1. Encode")
print("2. Decipher")
print("To quit, enter any other letter")
Choice = input("Enter the choice: ")
print("*************************************")

if Choice == 1:
		print("Playfair Encryption Tool (P.E.T)")
		print("Written By: Trey Brumley")
		print("*************************************")
		keyword = input("Please enter a keyword: ")
		print("*************************************")
		print()
		
		print("Playfair Encryption Tool (P.E.T)")
		print("Written By: Trey Brumley")
		print("*************************************")
		Message = input("Please enter a message: ")
		print("*************************************")
		print()
		
		playFair = generateSquare(keyword)
		
		print("Playfair Encryption Tool (P.E.T)")
		print("Written By: Trey Brumley")
		print("*************************************")
		print("Your encrypted message is:")
		encoded = encodeMessage(Message,playFair)
		print(encoded)
		print("*************************************")
		print()
		
elif Choice == 2:
		print("Playfair Encryption Tool (P.E.T)")
		print("Written By: Trey Brumley")
		print("*************************************")
		keyword = input("Please enter a keyword: ")
		print("*************************************")
		print()
		
		print("Playfair Encryption Tool (P.E.T)")
		print("Written By: Trey Brumley")
		print("*************************************")
		encoded = input("Please enter the encrypted message: ")
		print("*************************************")
		print()
		
		playfair = generateSquare(keyword)

		print("Playfair Encryption Tool (P.E.T)")
		print("Written By: Trey Brumley")
		print("*************************************")
		print("Your decrypted message is:")
		Message = decodeMessage(encoded,playFair)
		print(Message)
		print("*************************************")
		print()