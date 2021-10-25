#scramble words that are less than 3 characters in a file. 
#do NOT scramble punctuation or words greater than 3 characters.

from random import shuffle	

#STRING -> STRING	
def scramble(word):
	if len(word) < 4:
		return word
		
	#make sure we don't scramble ending punctuation
	ending = -1
	while not word[ending].isalpha():
		ending -= 1
	
	middle = word[1:ending]
	middle = list(middle)
	shuffle(middle)
	middle = ' '.join(middle)
	return word[0] + middle + word[-1]
	
#STRING -> None (print scrambled output)
def scramble_words(filename):
	with open(filename, 'r') as f:
		for line in f:
			text = ''
			for word in line.strip().split(' '):
				text += scramble(word) + ' '
			print(text)