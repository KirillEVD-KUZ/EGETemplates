for i in range (1,100000):
    b=bin(i)[2:]
    osum= b.count("1") %2
    b=b + f"{osum}"
    osum1=b.count("1") %2
    b=b+f"{osum1}"
    res= int(b,2)
    if res >97:
        print (res)
        break