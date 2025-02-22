for p in range(1, 100):
    for x in range(1, p):
        for y in range(0, p):
            for z in range(1, p):
                for w in range(1, p):
                    t1 = (y * p ** 3) + (2 * p ** 2) + (7 *p ** 1) + (x * p ** 0)
                    t2 = (w * p ** 3) + (y *p ** 2) + (8 * p ** 1) + (6 *p **0)
                    t3 = (x * p **4) + (x * p **3) + (z * p **2) + (3 * p **1) + (y * p **0)
                    if t1 + t2 == t3:
                        print(x * p ** 3 + y * p ** 2 + z * p ** 1 + w * p ** 0)
