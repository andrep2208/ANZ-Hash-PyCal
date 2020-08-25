import csv

class hashCal:
    def __init__(self):
        self.path= ""
        self.fileName = ""

    def saySomething(self):
        print("Something!")

    def setPath(self, path):
        self.path = path

    def setFileName(self, fileName):
        self.fileName = fileName

    def getPath(self):
        print(self.path)

    def doCalculate(self):
        result = 0
        accountList = []
        filePath = self.path + self.fileName
        with open(filePath, newline = '') as orginalFile:                                                                                          
            data = csv.reader(orginalFile, delimiter=',')
            for row in data:
                if(row[0] == "2"):
                    rowvalue = int(row[1][2:13])
                    result += rowvalue

        resultString = str(result)
        print("This is the hash number: " + resultString[-11:])