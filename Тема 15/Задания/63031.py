for A in range(1, 128):
    f=True
    for x in range (1, 128):
        if not ((( x & 57 > 0) or (x & 99 > 0)) <= ( x & A > 0)):
            f= False
            break
    if f:
        print(A)