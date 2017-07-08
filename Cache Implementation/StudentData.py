import GetInformation as g
import Main as m
import WriteFile as wf

class StudentData:

    def studentData(self, details):
        flag = False
        data = g.GetInformation().getInfo('input/student_database.tsv')
        try:
            flag = next(True for i in data if int(details[0]) == i[0])
        except:
            pass
        if not flag:
            wf.WriteFile('input/student_database.tsv').updateInFile(details)
            return m.Main().update + "New Record Added" + m.Main().end
        else:
            print m.Main().warning + "Data already exists in the database"
            q = raw_input(m.Main().update + "Do you want to update the existing record (y/n): " + m.Main().end)
            if q == "y":
                update_data = []
                [update_data.append(value) for value in data if int(details[0]) != value[0]]
                if isinstance(details, list):
                    update_data.append(details)
                    wf.WriteFile('input/student_database.tsv').writeInFile(update_data, m.Main().headers[:-1])
                return m.Main().update + "Data updated" + m.Main().end
            else:
                return m.Main().update + "No record updated" + m.Main().end