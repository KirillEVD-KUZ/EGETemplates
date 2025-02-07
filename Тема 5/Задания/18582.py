for i in range (1,1000):
    b=bin(i)[2:]
    b=str(b)
    if b.count("0") < b.count("1"):
        b+="1"
    else:
        b+="0"
    res= int(b,2)
    if res>100:
        print(res)
        break