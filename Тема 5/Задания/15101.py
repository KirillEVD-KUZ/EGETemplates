for i in range(1000, 10000):
    n = str(i)
    sum1 = int(n[0]) + int(n[1])
    sum2 = int(n[1]) + int(n[2])
    sum3 = int(n[2]) + int(n[3])
    srsum= (sum1 + sum2 + sum3) - max(sum1,sum2,sum3) - min(sum1,sum2,sum3)
    res= str(srsum) + str(max(sum1,sum2,sum3))
    if res == "1215":
        print(i)
        break
