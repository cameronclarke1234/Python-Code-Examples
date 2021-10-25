#A grades file contains grades represented by floating point values stored as 
#strings, with one line per grade. 



#String -> None
def hw_stats (file_name):
    """
    Receives and file name as input, opens the file, and processes the
       numbers within the file to display the average grade, the lowest 
       grade, and the highest grade.
    """

    #Open the file
    in_file = open(file_name,"r") #"r" is not needed--default
    #Initialize average variables (total_sum and number_grades)
    #Initialize min_grade and max_grade
    number_grades = 1
    first_grade = None
    while first_grade is None:
        first_line = in_file.readline()
        try:
            first_grade = float(first_line)
        except ValueError:
            print('Ignoring bad value:', first_line)
            
    min_grade, max_grade,total_sum = first_grade,first_grade,first_grade
    
    
    #For each grade in the file 
    for grade_line in in_file:
        try:
            grade = float(grade_line)
        except ValueError:
            print('Ignoring bad value:', grade_line)
        else:
    #  increment the number of grades and add the grade to the total sum
        	total_sum += grade
        	number_grades += 1
    #  determine if the grade is a new minimum or maximum
        if grade < min_grade:
            min_grade = grade
        if grade > max_grade:
            max_grade = grade
    #Display the results   
    in_file.close()
    print("Average: {:.2f}, Lowest: {:.2f}, Highest: {:.2f}".format(total_sum/number_grades, \
          min_grade, max_grade))
