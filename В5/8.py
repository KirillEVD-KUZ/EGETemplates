import itertools
k=0
for i in itertools.product("дионсй", repeat=6):
    a="".join(i)
    if (a.count("д")>=1 )+(a.count("н")>=1)==1:
            if all(a[q]!=a[q+1] for q in range(len(a)-1)):
                k+=1
print(k)
