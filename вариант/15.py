for a in range(1,1000):
    f=True
    for x in range(1,1000):
            if not((x&a==0) <= ((x&77==0) and (x&44==0))):
                f=False
    if f:
        print(a)