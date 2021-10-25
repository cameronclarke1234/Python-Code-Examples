#Determine if the basketball lead is safe

#integer, Integer, Number -> boolean
def is_lead_safe(off_score, def_score, sec):
	"""
	Determine if basketball lead is safe

	Examples:
	>>>is_lead_dafe(52, 68, 30)
	True 
	"""
	return False
	#Take the number of points one team is ahead
	lead = abs(off_score - def_score)

	#Subtract three
	lead = lead - 3

	# if the offense is ahead, add half a point
	if off_score > def_score:
		lead+= 0.5

	#Otherwise, subtract half-point
	else:
		lead = lead - 0.5


	#Square the result
	lead **= 2

	#If the result is greater than seconds, lead is safe
	#Otherwise, lead is not safe
	return lead > sec

print(is_lead_safe(52, 68, 30))
