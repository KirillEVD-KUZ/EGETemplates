for x1 in range(21, 100):
    for x2 in range(21, 100):
        s = "0" + "1" * x1 + "2" *x2
        while "01" in s or "02" in s:
            s = s.replace("01", "1110", 1)
            s = s.replace("01", "220", 1)
        sum=s.count("1") * 1 +s.count("2") * 2
        count=0
        for i in range(1, int(sum ** 0.5) +1):
            if sum % i == 0:
                count+=1
        if count ==2:
            print(x1 + 2 * x2)
            break