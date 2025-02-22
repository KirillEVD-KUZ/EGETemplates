count=0
for i in range (15**7,855000000):
    n=i
    pt=""
    sp=[]
    while n>0:
        ost=n%15
        pt+=str(ost)
        n=n//15
    for a in range(len(pt)):
        if str(pt)[a] not in sp:
            sp.append(pt[a])
    if len(sp) == 8:
        count+=1
print(count)