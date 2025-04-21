a=list(map(int,open("17_21416.txt").readlines()))
smo=0
for i in range(len(a)):
    if a[i]<0:
        smo+=a[i]
mx=0
sp=[]
for i in range(len(a)-2):
    ss=max(a[i],a[i+1],a[i+2])*min(a[i],a[i+1],a[i+2])
    if ss>smo:
        sp.append(abs(ss))
print(len(sp),max(sp))
