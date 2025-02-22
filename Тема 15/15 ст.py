for A in range(1, 10000):
    F = True
    for x in range(1, 10000):
        if not(((x & 5160 > 0) or (x & 3650 > 0)) <= ((x & 9545 == 0) <= (x & A > 0))):
            F=False
    if F:
        print(A)