a=open("24_21421.txt").readline()
sp=[]
ch=[0,1,2,3,4,5,6,7,8,9,"A","B"]
k=0
for i in range(len(a)):
    if i in ch:
        k+=1
    else:
        sp.append(k)
        k=0
print(sp)
