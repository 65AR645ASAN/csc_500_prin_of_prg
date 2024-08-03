class AttendanceManager:
    """Class to manage and calculate attendance records."""

    def __init__(self, attendance_list):
        """
        Initialize the AttendanceManager with an attendance list.

        Args:
        attendance_list (list of bool): List containing attendance records (True for present, False for absent).
        """
        self.attendance = attendance_list

    def count_days_present(self):
        """
        Count the number of days present in the attendance list.

        Returns:
        int: The number of days present.
        """
        return self.attendance.count(True)

    def display_days_present(self):
        """Display the number of days present."""
        days_present = self.count_days_present()
        print("Days present:", days_present)



attendance_list = [True, True, False, True, True, False, True]
attendance_manager = AttendanceManager(attendance_list)

attendance_manager.display_days_present()
