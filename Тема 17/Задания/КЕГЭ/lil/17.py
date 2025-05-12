"""a=list(map(int,open("17_19249.txt").readlines()))
mx=-100001
for i in range(len(a)):
    if 10000<=abs(a[i])<100000 and abs(a[i])%100==43:
        mx=max(mx,a[i])
mns=[]
for q in range(len(a)-2):
    if ((10000<=abs(a[q])<100000 and abs(a[q])%100==43)+(10000<=abs(a[q+1])<100000 and abs(a[q+1])%100==43)+(10000<=abs(a[q+2])<100000 and abs(a[q+2])%100==43))>0:
        if (a[q]**2 +a[q+1]**2+a[q+2]**2)<=mx**2:
            mns.append(a[q]**2 +a[q+1]**2+a[q+2]**2)
print(len(mns), min(mns))"""
"""#18957
a=list(map(int,open("17_18957.txt").readlines()))
mxp=max(a)
sp=[]
for i in range(len(a)-2):
    if (("0" not in str(a[i]))+("0" not in str(a[i+1]))+("0" not in str(a[i+2])))>=2:
        if a[i]+a[i+1]+a[i+2]<mxp/2:
            sp.append(a[i]+a[i+1]+a[i+2])
print(len(sp),max(sp))"""
"""#Решу егэ 37340
a=list(map(int, open("17 (1).txt").readlines()))
sp=[]
for i in range(len(a)-1):
    for q in range(i+1,len(a)):
        if abs(a[q]-a[i])%2==0:
            if ((a[i]%31==0)+(a[q]%31==0))>=1:
                sp.append(a[q]+a[i])
print(max(sp), len(sp))
#19982 1569269
"""
#Решу егэ 37337
a=list(map(int,open("17-428.txt").readlines()))
a13=0
k=0
a25=0
for q in range(len(a)+1):
    if q%13:
        k+=1
    if k==13:
        a13=q
a13=sum(map(int,str(a13)))
k=0
for p in range(len(a)+1):
    if p%13:
        k+=1
    if p==13:
        a25=p
a25=sum(map(int,str(a25)))

for i in range(len(a)-2):
    if ((len(str(a[i]))==3)+(len(str(a[i+1]))==3)+(len(str(a[i+2]))==3))>=1:
        if sum(map(int, str(a[i])))



