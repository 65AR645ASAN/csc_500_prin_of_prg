grades = [90, 100, 80, 95, 78, 'aditya', 'curtis']


def add_grade(grade):
    grades.append(grade)


def get_average():
    total = 0
    count = 0  # Count only the valid integer grades
    for grade in grades:
        if isinstance(grade, int):
            total += grade
            count += 1

    if count > 0:
        grade_average = total / count
    else:
        grade_average = 0

    return grade_average


print("Grade Average is:", get_average())
add_grade(100)
print("New Grade Average is:", get_average())
