'''
Ask user for grades filename. Read in grades from 
given file, compute statistics, and print.
'''

def file_stats():
	# Ask user for filename
	filename = input('grades.txt')
	
	# Make a list to hold the grades
	grades = []
		
	# Open that indicated file
	with open(filename, 'r') as f:
	
		#Read each line and change it to a float
		for line in f:
			try:
				line = float(line)
			except ValueError:     #When the line if not a float
				print('Ignoring bad value:', line[:-1])
			else:  
				grades.append(float(line))