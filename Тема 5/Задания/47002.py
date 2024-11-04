for N in range(0,1000):
    b=bin(N)[2:]
    num1=b[::2].count("1")
    num0=b[1::2].count("0")
    res=abs(num1-num0)
    if res==4:
        print(N)
        break