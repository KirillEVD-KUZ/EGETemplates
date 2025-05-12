mn=10000000
for i in range(100000000,1000000000000):
    b=bin(i)[2:]
    dv=str(b).lstrip("0")
    k0=dv.count("0")
    k1=dv.count("1")
    b0=str(bin(k0)[2:]).lstrip("0")
    b1=str(bin(k1)[2:]).lstrip("0")
    r=f"{b1}{b0}"
    res=int(r,2)
    if res==214:
        print(i)