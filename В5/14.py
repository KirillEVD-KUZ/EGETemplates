for a in range(1,100000000):
    for x in "0123456789ABCDE":
        m=int(f"432{x}3",15)
        n=int(f"86{x}86",15)
        if (m+a)%n==0:
            print(a)