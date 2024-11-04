for N in range(1, 100000):
    b = bin(N)[2:]
    b=b.replace("1","i").replace("0","1").replace("i","0")
    b = int(b, 2)
    res = N - b
    if res == 999:
        print(N)
        break

