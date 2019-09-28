a=input()
b=input()
a=a.split()
b=b.split()
finalList=[]
countA=0
countB=0
if int(a[0])>int(b[0]):
	countA+=1
if int(a[0])<int(b[0]):
	countB+=1
if int(a[0])==int(b[0]):
	countA+=0
	countB+=0
if int(a[1])>int(b[1]):
	countA+=1
if int(a[1])<int(b[1]):
	countB+=1
if int(a[1])==int(b[1]):
	countA+=0
	countB+=0
if int(a[2])>int(b[2]):
	countA+=1
if int(a[2])<int(b[2]):
	countB+=1
if int(a[2])==int(b[2]):
	countA+=0
	countB+=0
finalList.append(countA)
finalList.append(countB)
print(finalList[0],finalList[1])
