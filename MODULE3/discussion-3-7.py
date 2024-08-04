grades = [90, 100, 80, 95, 78]

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



