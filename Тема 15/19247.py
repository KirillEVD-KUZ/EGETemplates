for a in range (1500):
    f=True
    for x in range (1,1500):
        for y in range(1,1500):
            if not(((x - 3*y) <a) or (y >400) or (x > 56)):
                f= False
    if f:
        print(a)
        break