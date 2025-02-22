# y18x + wy98 = xxz4y.

for p in range(1, 10):
    for x in range(1, p):
        for y in range(1, p):
            for z in range(1, p):
                for w in range(1, p):
                    t1 = (y * p ** 3) + (1 * p ** 2) + (8 * p ** 1) + (x * p ** 0)
                    t2 = (w * p ** 3) + (y * p ** 2) + (9 * p ** 1) + (8 * p ** 0)
                    t3 = (x * p ** 4) + (x * p ** 3) + (z * p ** 2) + (4 * p ** 1) + (y * p ** 0)
                    if 