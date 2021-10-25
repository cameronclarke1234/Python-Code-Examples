#accepts a file name string and a boolean value as input. 
#The function reads the file and, if the boolean argument is True, 
#it returns a nested list in which each row is a list of words in a single line.

#files, boolean -> return bool, nested list
def get_text(filename, bool):
    #open the filename 
    new_file = open(filename, 'r')
    #commands for the boolean value
    if bool == True:
        #open list 'a'
        alist = []
        for line in new_file:
            text = line.strip().split(' ')
            lists = list(text)
            #add the changes to the text in the lines to the list
            alist.append(lists)
        return alist
    else:
        for item in new_file:
            tuplelist += (tuple(item.split()))
        return tuplelist