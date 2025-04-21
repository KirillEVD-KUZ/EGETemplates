a=list(map(int,open("17.txt").readlines()))
mn=100000
for q in range(len(a)-1):
    if a[q]%1000==123 and a[q]<mn:
        mn=a[q]
k=0
mx=140
for i in range(len(a)-1):
    if a[i]+mn>=a[i+1] or a[i]-mn>=a[i+1]:
        k+=1
print(k)
