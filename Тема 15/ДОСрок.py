for a in range(1, 100):
    f = 1
    for x in range(1, 100):
        for y in range(1, 100):
            if not ((5 < y) or (x > 32) or ((x + (2 * y)) < a)):
                f = 0
    if f:
        print(a)
