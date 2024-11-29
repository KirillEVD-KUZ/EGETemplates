result = []
for N in range(1,49):
    b=bin(N)[2:]
    ost=N%4
    b_ost=bin(ost)[2:]
    res_b= b + b_ost
    res=int(res_b ,2)
    result.append(res)