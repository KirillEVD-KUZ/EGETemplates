min=100000
for x in range(1, 100000):
    tr = ""
    tu = x
    while tu > 0:
        tr += str(tu % 3)
        tu //= 3
    tr = tr[::-1]
    if x %3==0:
        tr=tr[-2:]+tr
    sm=0
    if x%3!=0:
        sm=tr.count("2")*2+tr.count("1")*1
        tr1=""
        while sm>0:
            tr1+=str(sm%3)
            sm//=3
        tr1=tr1[::-1]
        tr=tr1+tr
    r=int(tr,3)
    if r>418:
        if r<min:
            min=r
print(min)