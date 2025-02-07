for i in range(100,1000):
    i=str(i)
    sum1=int(i[0])+int(i[1])
    sum2=int(i[1])+int(i[2])
    mk=max(sum1,sum2)
    mn=min(sum1,sum2)
    res=f"{mn}{mk}"
    if res == "1115":
        print(i)
        break