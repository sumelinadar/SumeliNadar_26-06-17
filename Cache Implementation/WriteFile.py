import csv
import os

class WriteFile:

    def __init__(self, filename):
        self.path = os.path.abspath(filename)

    def writeInFile(self, data, headers):
        with open(self.path, 'w') as f:
            writer = csv.writer(f, delimiter='\t', lineterminator='\n')
            writer.writerow(headers)
            for value in data:
                writer.writerow(value)

    def updateInFile(self, data):
        with open(self.path, 'a+') as f:
            writer = csv.writer(f, delimiter='\t', lineterminator='\n')
            writer.writerow(data)