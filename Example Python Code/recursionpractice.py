#FIBONACCI SEQUENCE

def fib(n, d):
	if n not in d:
	    d[n] = fib(n-1, d) + fib(n-2, d)
	return d[n]
    
fib(5, {0:1, 1:1})





# 'madam'
# 'bob'
# 'racecar'
def pal(letters):
    if len(letters) < 2:
        return True
    elif:
        if letters[0] == letters[-1]:
            if pal(letters[1:-1]):
                return True
    else:
        return False
        
        
        
        
#SMALLEST NUMBER OUT OF A LIST RECURSION
def rec_min(list1):
    if len (list1) < 2:
        return list1[0]
    
    if list1[0] < rec_min(list1[1:]):
        return list1[0]
    
    else:
        return rec_min(list1[1:])
        
rec_min([5,4,3,2])

        
        
        
#BEAT NAVY
def bn(n):
    if n < 1:
        return "Beat Navy!"
    return "Beat" + bn(n-1)

print(bn(3))





def tot(s):
    if not s:
        return 0
    if s[0].isdigit():
        return int(s[0]) + tot(s[1:])
    return tot(s[1:])



#COUNT-UP, COUNT-DOWN
def count_up(n):
    if n <= 0:
        print(0)
    else:
        print(n)
        count_up(n-1)
    
count_up(4)
