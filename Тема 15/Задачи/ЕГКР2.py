for A in range(1,1000000):
    B=True
    for x in range(1,100000):
        if (x & 6280> 0  or x&3394>0) and not(x &10828 == 0 <= x & A >0):
            B=False
    if B:
        print(A)
        break
