
for N in range (99,200):
    b=bin(N)[2:]
    for i in range(3):
        num1=b.count("1")
        num0=b.count("0")
        if num1 == num0:
            b+=b[-1]
        elif num1<num0:
            b+="1"
        else:
            b+="0"
    res=int(b,2)
    if res % 4 == 0:
        print(N)
        break