import math
listA=[]
numberOfStudents=int(input())
for i in range(numberOfStudents):
    listB=[]
    line=input()
    listB.append(line)
    line=float(input())
    listB.append(line)
    listA.append(listB)


listOfNumbers=[]
for i in range(len(listA)):
    listOfNumbers.append(listA[i][1])
listOfNumbers.sort()
minNumbers=listOfNumbers[0]


minNumber=math.inf
names=[]
for i in range(len(listA)):
    theNumber=listA[i][1]
    if theNumber!=minNumbers:
        if theNumber<minNumber:
            names=[]
            names.append(listA[i][0])
            minNumber=theNumber
        elif theNumber==minNumber:
            names.append(listA[i][0])
names.sort()
for i in names:
    print(i)

