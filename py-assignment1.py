num_of_courses = int(input("How many courses did you finish? "))
course_marks = 0
for n in range(num_of_courses):
    numbers = float(input("Enter your mark for course : "))
    course_marks += numbers
    average = course_marks/num_of_courses
print("Your average for ", num_of_courses, " courses is :", average)