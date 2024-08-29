# COPY THIS LINE OF CODE - BEGINNING
def main():
    university_instruction_rooms = {
        'CSC101': '3004',
        'CSC102': '4501',
        'CSC103': '6755',
        'NET110': '1244',
        'COM241': '1411'
    }

    professors = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee'
    }

    instruction_time_slots = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.'
    }

    subject_number = input("Enter a subject number (e.g., NET110): ")

    if subject_number in university_instruction_rooms:
        print(f"Course Number: {subject_number}")
        print(f"Room Number: {university_instruction_rooms[subject_number]}")
        print(f"Instructor: {professors[subject_number]}")
        print(f"Meeting Time: {instruction_time_slots[subject_number]}")
    else:
        print("Sorry, the course number entered does not exist.")


if __name__ == "__main__":
    main()
# COPY THIS LINE OF CODE - ENDING
