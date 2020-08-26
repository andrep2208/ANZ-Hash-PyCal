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
        currentHash = ""
        accountList = []
        filePath = self.path + self.fileName
        with open(filePath, newline = '') as orginalFile:                                                                                          
            data = csv.reader(orginalFile, delimiter=',')
            for row in data:
                if(row[0] == "2"):
                    rowvalue = int(row[1][2:13])
                    result += rowvalue
                
                elif (row[0] == "3"):
                    currentHash = row[3]

        resultString = str(result)

        if(resultString == currentHash):
            print("The current has number is correct: " + currentHash)
        else:
            print("This is the hash number: " + resultString[-11:])
            print("This is the current has number: " + currentHash)