import itertools
sp=[]
mx=0
o1=0
k=0
for o in range(1,20):
    for i in itertools.product("01",repeat=20):
        a="".join(i)
        if a.count("0")==o:
            k+=1
    if 100000<=k<=1000000:
        mx=k
        o1=o
    k=0
print(o1,mx)
