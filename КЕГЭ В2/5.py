mn=1000
for n in range(1, 10000):
    n1 = n
    tr = ""
    while n1 > 0:
        tr += str(n1 % 3)
        n1 //= 3
    tr = tr[::-1]
    sm=tr.count("1")+(tr.count("2")*2)
    if sm%2==0:
        tr=f"1{tr}2"
    if sm%2!=0:
        tr=f"2{tr}0"
    res=int(tr,3)
    print(n,tr,res)
    if mn>res and res>100:
        mn=res
print(mn)