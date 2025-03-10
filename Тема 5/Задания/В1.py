mn=10000000
for n in range(1,1000000):
    b=bin(n)[2:]
    if n%2==0:
        b="1"+b+"00"
    if n%2!=0:
        bn1=bin(b.count("1"))[2:]
        b=b+str(bn1)
    res=int(b,2)
    if res>205:
        if mn>res:
            mn=res
print(mn)