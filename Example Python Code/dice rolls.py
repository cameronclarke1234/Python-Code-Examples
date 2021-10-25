from random import randint


#keeping track of dice numbers and dice rolls


#Die roll: INT
#Rolls: LIST


#INT -> NONE (print histogram)
def plot_dice(n, k):

	rolls = []
	 
	# roll die n times
	for _ in range(n):
		rolls.append(randint(1, k))
	
	# Count each number from rolls
	counts = []
	for i in range(1, k + 1):
		counts.append(rolls.count(i))
	print(counts) 
	
	# print histogram
	for label, count in enumerate(counts):
		print(index + 1, '|', 'x' * count, count)
