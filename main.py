#by Andre P

from hashCal import hashCal

if __name__ == "__main__":

    path = input("what is the path? e.g (C:\\Users\\) ")
    fileName = input("what is the file name (with extension)? (e.g test.txt) ")
    newCal = hashCal()
    newCal.setPath(path)
    newCal.setFileName(fileName)
    newCal.doCalculate()