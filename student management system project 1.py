# Function to get student data
def get_student_data():
    name = input('Enter your name : ')
    age = int(input('Enter your age :'))
    city = input('Enter your city :')
    course = input('Enter your course :')
    marks = int(input('Enter your marks :'))

    return name,age,city,course,marks

# Function to calculate grade

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"

# Function to get remarks

def get_remarks(grade):
    if grade == 'A+':
        return "Excellent"
    elif grade == 'A':
        return "Very Good"
    elif grade == 'B':
        return "Good"
    elif grade == 'C':
        return "Need Improvement"
    else:
        return "Better Luck Next Time"

# Function to check status

def get_status(marks):
    if marks >= 60:
        return 'Passed'
    else:
        return 'Failed'

# Functio to display student output

def display_student(name, age, city, course, marks,grade,remarks,status):
    print("\n----- Student Information -----\n")
    print(f'Name   : {name}')
    print(f'Age    : {age}')
    print(f'City   : {city}')
    print(f'Course : {course}')
    print(f'Marks  : {marks}')
    print(f'Grade  : {grade}')
    print(f'Remarks: {remarks}')
    print(f'Status : {status}')

#  Main function

name, age, city, course, marks = get_student_data()
grade = calculate_grade(marks)
remarks = get_remarks(grade)
status = get_status(marks)
display_student(name, age, city, course, marks, grade,remarks,status)
