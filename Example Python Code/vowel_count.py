 #Count the number of vowels
 	#string.lower
 	#vowels (aeiou)

 def vowel_shift():
 	count = 0
 	for i in string.lower():
 		if i in "aeiou":
 			count += 1
 	return count