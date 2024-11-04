for N in range (1,3000):
    b=bin(N)[2 : -1]
    if N %2 ==0:
        b+="01"
    else:
        b+="10"
    res=int(b,2)
    if res == 2018:
        print(N)

