i=9 
while True:
    b=bin(i)[2:]
    c1=bin(b.count("1"))[2:]
    c0=bin(b.count("0"))[2:]
    res=int(c1 +c0,2)
    if res == 214:
        break
    print(i, res)
    i+=10
print(i)
