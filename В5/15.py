for a in range(1, 1000):
    f = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((not ((x < 7) or (y >= ((5 * x) + a - 60)) or (x >= 36) or (y < 225)))):
                f = 0
    if f:
        print(a)
