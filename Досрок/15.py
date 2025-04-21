for a in range(1,300):
    f=True
    for x in range(0,300):
        for y in range(0,300):
            if not((5<y) or (x>32)or (x+2*y)<a):
                f=False
    if f:
        print(a)