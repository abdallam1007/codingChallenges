numberOfLines=int(input())
listA=[]
for i in range(numberOfLines):
    line = input()
    line=line.split()
    A=line[0]
    if A=="insert":
        listA.insert(int(line[1]),int(line[2]))
    if A=="print":
        print(listA)
    if A=="remove":
        listA.remove(int(line[1]))
    if A=="append":
        listA.append(int(line[1]))
    if A=="sort":
        listA.sort()
    if A=="pop":
        listA.pop()
    if A=="reverse":
        listA.reverse()
