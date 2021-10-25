#user has to guess a number between 1-100. The user has 20 tries to guess the correct answer.

import random

#number of guesses: Integer
#Secret number: Integer
#guessed number: Integer
#Return a boolean
#	- True if win
#	- False if lose

# None -> Boolean
def twenty_questions():
	"""
	Give user 20 guesses for number 1-100
	"""	
	#Start counting guesses (from 0)
	guesses = 0

	# Pick a random number between 1 and 100
	secret = random.randint(1,100)

	#Check if guesses are less than 20
	while guesses < 20:

	#Ask the person to guess that number
	num = int(input('Guess a number [1-100]:'))

	#Compare guess with pick
	#tell person right or wrong
	if num == secret:
	#if right, the person wins 
		print('nice!')
		guesses += 20
		return True
	else:
	#If wrong,
	#	+ add one to guesses used 
		guesses += 1
	#	+ guess again (go back to the check step) 
		print('Try again.')

	#if no, the person losses (GAME OVER)
		print('GAME OVER')
		return False


print(twenty_questions())
