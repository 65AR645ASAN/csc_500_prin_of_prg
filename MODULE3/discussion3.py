class StudentGrades:
    def __init__(self, grades):
        self.grades = grades

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def find_highest(self):
        return max(self.grades)

    def find_lowest(self):
        return min(self.grades)

    def print_grades_info(self):
        average_grade = self.calculate_average()
        highest_grade = self.find_highest()
        lowest_grade = self.find_lowest()

        print(f"Average grade: {average_grade}")
        print(f"Highest grade: {highest_grade}")
        print(f"Lowest grade: {lowest_grade}")

# Example usage
grades = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
student_grades = StudentGrades(grades)
student_grades.print_grades_info()



