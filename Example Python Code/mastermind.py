#MASTERMIND GAME

#Data Representation
	#Colors: Single character strings
	#Secret: string
	#Guess: String
	#number of guesses: Integer


#None -> none
import random

def mastermind():
	"""
	Mastermind Game
	Computer genetates a secret sequence of k (default 4) colors, chosen randomly from a set of n (default 6) colors (default no repeated colors). Human player has a g (default 12) guesses to correctly recreate the secret sequence.
	"""
	#Generate a secret
	secret = ""
	while len(secret) < 4:
	letter = random.choice("GBPROY")
	if letter not in secret:
		secret += letter
	print(secret)
	#Allow guesses
	for _ in range(12):
		guess = input("Enter a guess")
		#If guess matches secret, print winning message and quit
		if guess == secret:
			print("You Win!")
			return
		else:
			print(feedback(guess, secret))
	#print losing message
	print("You Lose")


def feedback(guess, secret):
	"""
	Print mastermind feedback based on two strings
	"""
	
	count_b = 0
	count_w = 0
	#Loop through both strings at the same time, character by character 
	for char in range(min(len(guess), len (secret))):
		#If the string character equals the guess character, add a black dot.
		if secret[i] == guess[i]
			count_b += 1
		elif guess[i] in secret:
			count_w += 1
	#Return a string of the correct number of black dots
	return "B" * count_b + "W" * count_w
	
