# Kiu Man Yeung, 118100055

# Question 1
def calculate_results(students):
    # A function to print the min max and mean score for each student, the overall high score and overall award achieved by each student.  It takes a list of students with their list of marks as a variable, returns 0 on success
    # I am assuming that overall award achieved by each student means to count the number of 1H, 2.1, 2.2, passes achieved in total by all students

    # Initialize overall count of high score, number of 1H 2.1 2.2 and pass
    # Overall high cannot be set to a specific number because it is compared to and reassigned 
    overall_high = students[0][1][0]
    overall_1H = 0
    overall_21 = 0
    overall_22 = 0
    overall_pass = 0

    # Loop thruogh the list of students
    for student in students:
        # Initialize max min and sum of marks for each students
        max_marks = student[1][0]
        min_marks = max_marks
        sum_marks = 0
        # Loop through all the marks of a particular student
        for marks in student[1]:
            # Add all marks to sum_marks
            sum_marks += marks
            # Compare the mark to the current max and min, update the max and min when applicable
            if marks > max_marks:
                max_marks = marks
            if marks < min_marks:
                min_marks = marks
            # Classify the mark and add it to the overalls
            if marks >= 70:
                overall_1H += 1
            elif marks >= 60:
                overall_21 += 1
            elif marks >= 50:
                overall_22 += 1
            elif marks >= 40:
                overall_pass += 1
        # If the mark is higher than overall_high, update oevrall_high
        if max_marks > overall_high:
            overall_high = max_marks
        # Calculate the average mark using the sum of marks and the number of marks
        mean_marks = sum_marks / len(student[1])
        print (student[0], max_marks, mean_marks, min_marks)
    print ("\nHigest: %d" % overall_high)
    print ("1H: %d\t2.1: %d\t2.2: %d\tpass: %d" % (overall_1H, overall_21, overall_22, overall_pass))
    return 0