for N in range(34722222, 34722224):
    b=bin(N)[2:]
    ost=N % 3
    b_res=b+(bin(ost)[2:].zfill(2))
    res=int(b_res,2)
    ost_res=res % 5
    c_res=bin(ost_res)[2:].zfill(3)
    ans= b_res + c_res
    print(ans)
