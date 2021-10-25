#Running the simulation n times means we need to run it once.
#Needle poisition described by x-coordinate and angle 

#STEP 1: Analysis -> Data Representaiton
#X is a float
#Angle is a float
#Endpoint is a float
#Result is a boolean (True = crossed a line)

import math

#Step 2: Purpose, signature, stub
#Float, float -> Boolean
def drop (X, angle):
	'''
	Did the needle cross a line or not?
	
	Step 3: Examples (and Step 6: Test)
	>>> drop(0.1, math.radians(140))
	true
	>>> drop(0.1, math.radians(140))
	false
	'''
	# Calculate the endpoint: x + cos(angle)\
	endpoint = x + math.cos(angle)
	# If x < 0 or x > 1, return True
	if endpoint < 0 or endpoint > 1:
		return True
	#Otherwise, return False
	return False


#STEP 1: Analysis -> Data Representaiton
#X is a float
#Angle is a float
#Result is a boolean (True = crossed a line)

#Step 2: Purpose, signature, stub
#None, -> Boolean

def test():
	''' 
	Drop a needle randomly and test if it crossed a line
	'''
	#Get a random x [0, 1) --> random.random()
	x = random.random()
	#get a random angle [0,  180) --> random.random() * 180
	angle = random.random() * 180
	#Convert angle to radians (math.radians())
	angle= math.radians(angle)
	#Call drop with x and and angle (and return the result)
	return drop (x, angle)
	
	
#STEP 1: Analysis -> Data Representaiton
#N is an Integer
#Count is a Integer
#Result is a float

#Step 2: Purpose, signature, stub
#Integer -> Float
def buffon(n):
	'''
	Run Buffon's needle test n times and approximate Pi
	'''
	#Start counting at zero
	count = 0
	#Loop n times
	for _ in range(n):
	#Call test()
		if test():
	#If result is true, add 1 to count
			count +=1
			#Do the math
			pi = 2 * n / count
			print(pi)
	
