def get_stop_words(filename):
#takes file name
#returns list of words

    results = []
    with open(filename,'r') as f:
        for line in f:
            for word in line.split(','):
                if len(word) > 3:
                    results.append(word)
    return results
        
def rm_punct(word):
    result = ''
    for c in word:
        if c not in '?.:;,!()"':
            result += c
    return result
    
def make_dict(filename, stop_words):
    
    with open(filename,'r') as f:
        for line in f:
            for word in line.split(','):
                word = rm_punct(word.strip())
                if len(word) > 3:
                    if word not in result:
                        result[word] = 0
                    result[word] += 1
    return result
                    
                    
def print_dict(words):
    for word in words:
        if words[word] > 3:
            print(word)
                       
               
