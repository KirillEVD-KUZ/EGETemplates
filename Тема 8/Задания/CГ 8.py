count1=0
for i in range(170859375, 855000000):
    pt=""
    n=i
    while n >0:
        pt+=str(n%15)
        n=n//15
    ch=[]
    count=0
    for y in range(len(pt)):
        if pt[y] not in ch:
            ch.append((pt[y]))
            count+=1
    if len(ch) == 8:
        count1+=1
print(count1)