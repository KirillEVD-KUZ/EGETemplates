mn=100000
for i in range(1,1000000):
    x=""
    b=bin(i)[2:]
    if b.count("1")%2==0:
        x=b+"0"
        x="10"+x[2:]
    if b.count("1")%2!=0:
        x=b+"1"
        x="11"+x[2:]
    r=int(x,2)
    if r>480 and i<mn:
        mn=i
print(mn)
