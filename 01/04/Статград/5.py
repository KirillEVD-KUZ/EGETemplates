mx=0
for i in range(1, 10000):
    tr = ""
    x = i
    while x > 0:
        tr += str(x % 3)
        x //= 3
    tr = tr[::-1]
    sm=tr.count('1')+(tr.count("2")*2)
    if sm%3==0:
        tr="112"+tr[2:]
    if sm%3!=0:
        tr1=""
        while sm>0:
            tr1+=str(sm%3)
            sm//=3
        tr1=tr1[::-1]
        tr=f"{tr}{tr1}"
    r=int(tr,3)
    if r>mx and r<=679:
        mx=r
print(mx)

