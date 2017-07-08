import pandas as pd
import os

class GetInformation:

    def dataFrame(self, filename):
        path = os.path.abspath(filename)
        df = pd.read_csv(path, sep="\t")
        return df

    def getInfo(self, filename):
        data = []
        for i in self.dataFrame(filename).iterrows():
            data.append(list(i[1].values))
        return data

    def getSpecificInfo(self, filename, student_id):
        for i in self.dataFrame(filename).iterrows():
            if student_id == list(i[1].values)[0]:
                return list(i[1].values)
        return "The records cannot be cached as it is not present in student database"