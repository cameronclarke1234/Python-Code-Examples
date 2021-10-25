# write a function named average_100_numbers() that computes the average of the 
# numbers 1 through (and including!) 100

# Step 1: Analysis -> Data representation
	#Need an integer for the number of the numbers in the list
	#Need a list of integers from 1 to 100 
	#Need an integer that is the sum
	#Need a float that is the average
	
# Step 2: Signature, Stub, Purpose
# None -> Float
def average_100_numbers():
	'''
	computes the average of the numbers 1 through (and including!) 100
	
	STEP 3: Examples / STEP 6: Test
	>>>average_100_numbers()
	50.5
	'''
	# STEP 4: Psuedocode
	# Start with 0
	total = 0
	# Add 1, then 2, then 3, then... 100
	for i in range(1,101):
		total += i
	# Divide by 100
	average = total/100
	# Return the result 
	return average
	

def average_1_to_x():
	'''
	computes the average of the numbers 1 through (and including!) 'x'
	
	STEP 3: Examples / STEP 6: Test
	>>>average_100_numbers()
	50.5
	'''
	# STEP 4: Psuedocode
	# Start with 0
	total = 0
	# Add 1, then 2, then 3, then... 100
	for i in range(1, x+1):
		total += i
	# Divide by 100
	average = total/x
	# Return the result 
	return average
