class StudentDetails:
    def studentDetails(self, action):
        details = map(int, raw_input("Enter the student ID for which you want to " + action + " the record").split())
        return details
