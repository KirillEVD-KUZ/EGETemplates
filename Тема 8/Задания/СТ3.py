k=0
for x in range(144,1000):
    a=""
    b=""
    x1=str(x)
    for i in range(len(x1)-1):
        if x1[i+1]>x1[i]:
            b+=str(x1[i])
    a+=""
    if a==b:
        k+=1
print(k)