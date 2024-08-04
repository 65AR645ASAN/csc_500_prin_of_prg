

# Array that holds grades for a course
grades = [90, 100, 80, 95, 78]

def add_grade_and_get_average(grade):
    grades.append(grade)
    total = sum(g for g in grades if isinstance(g, int))
    grade_average = total / len(grades)
    return grade_average

# Initial grade average
initial_average = add_grade_and_get_average(0)  # Using 0 as a placeholder; the grade won't be appended since it's not called
print("Grade Average is:", initial_average)

# Adding a new grade and getting the new average
new_average = add_grade_and_get_average(100)
print("New Grade Average is:", new_average)


grades = [90, 100, 80, 95, 78, 55, 60, 92, "sdfgsdfg"]

def add_grade(grade):
    grades.append(grade)

def get_average():
    total = 0
    for grade in grades:
        if isinstance(grade, int):
            total += grade
        grade_average = total / len(grades)
    return grade_average

print("Grade Average is:", get_average())
add_grade(100)
print("New Grade Average is:", get_average())


grades = [90, 100, 80, 95, 78 ]

def add_grade(grade):
    grades.append(grade)

def get_average():
    total = 0
    for grade in grades:
        if isinstance(grade, int):
            total += grade
    grade_average = total / len(grades)
    return grade_average

print("Grade Average is:", get_average())
add_grade(100)
print("New Grade Average is:", get_average())