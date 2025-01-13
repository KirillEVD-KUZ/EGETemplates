for a in range (1, 10000):
    
    for x in range(50):
        for y in range(50):
            if (((2*x) +(3*y)) <a) or (x >= y) or (y >=24) == True:
                print(a)
                break
