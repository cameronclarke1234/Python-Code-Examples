#Find the smallest number in a list of numbers

def list_min(numbers):
	lo = numbers[0]
	
	# check each number against minimum
	for number in numbers:
		# if it is smaller, it is new minimum
		if number < lo:
			lo = number
	
	# give the result:
	return lo