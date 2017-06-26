import CacheUpdate as u
import CacheDelete as d
import StudentDetails as s
import GetInformation as g
import StudentData as sd

class Main:
    def __init__(self):
        self.headers = ['Student_ID', 'Division', 'Marks', 'Recently_Viewed']
        self.options = "\033[94m"
        self.end = "\033[0m"
        self.OKGREEN = "\033[92m"
        self.warning = "\033[91m"
        self.update = "\033[95m"

    def userInput(self):
        main_action = input("Enter the action code: " + self.options + "1. To be performed on cache, 2. To be performed on student_database(Only to add new record for a student)" + self.end)
        if main_action == 1:
            action = input("Enter the action code to be performed on cache: " + self.options + "1. Update, 2. Delete, 3. Read" + self.end)
            if action == 1:
                print u.CacheUpdate().updateCache(s.StudentDetails().studentDetails("Update"))
            if action == 2:
                print d.CacheDelete().deleteCache(s.StudentDetails().studentDetails("Delete"))
            if action == 3:
                print self.update
                print g.GetInformation().dataFrame('input/cache_file.tsv')
                print self.end
        if main_action == 2:
            details = raw_input("Enter the student details in following order in a single row with space separated: " + self.OKGREEN + "student_id, division, marks" + self.end).split()
            if not details:
                print self.warning + "Kindly enter student record to be added in a proper format"
            else:
                sd.StudentData().studentData(details)


if __name__ == '__main__':
    m = Main()
    m.userInput()