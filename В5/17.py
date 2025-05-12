a = list(map(int, open("17_18957.txt").readlines()))
mx=0
for m in range(len(a)):
    if a[m]>mx:
        mx=a[m]
mx=mx/2
sp=[]
for i in range(len(a) - 2):
    q = str(a[i])
    p = str(a[i + 1])
    e = str(a[i + 2])

    if (("0" not in q) + ("0" not in p)+("0" not in e))>=2:
        if (a[i]+a[i+1]+a[i+2])<mx:
            sp.append((a[i]+a[i+1]+a[i+2]))
print(len(sp),max(sp))

