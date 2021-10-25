#Find the highest number in a list

def list_max():

	lo = numbers[0]
	
	# check each number against minimum
	for number in numbers:
		# if it is smaller, it is new minimum
		if number > lo:
			lo = number
	
	# give the result:
	return lo