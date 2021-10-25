# STR (filename) -> DICT (x-number: name)

def readfile(filename):
	result = {}
	with open(filename,'r') as f:
		for line in f:
			data = (line.split(','))
			result[data[0].strip()] = data[1].strip()
	return result
	

# DICT -> NONE (print each key-value pair as <key>: <value>)
def print_dict(db, search_str):
	"""
	>>> print_containing(readfile('xnums.txt'), 'u')
	x00000: William Punch
	x44444: Mark Lutz
	x33333: Timothy Boyd
	"""
	for key, val in db.items():
		if search_str in val.lower():
			print(key + ':', val)
			
			
def print_containing(db, search_str):
	for key, val in db.items():
	if search_str.lower() in val:
		
def print_values_sorted(db):
	for value in sorted(db.values()):
	print(value)
		
def print_sorted_by_value(db):
	for value in sorted(db.values()):
		for key in db:
			if db[key] == value:
				k = key
				break
		print(k + ':', value)
		#OR
		
	# for keys in db.keys():
	#for key in db:
		#print(key + ':', db[key])
