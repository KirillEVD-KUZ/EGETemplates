x=11
x1=x
tr=""
if x%3==0:
    tr=tr+str(tr[-1])+ str(tr[-0])
if x%3!=0:
    sm=tr.count("1")+ tr.count("2")
    tr1=""
    while sm > 0:
        tr1 += str(sm % 3)
        sm //= 3
    tr1 = tr1[::-1]
    tr=tr+str(tr1)
    for y in range(len(tr)):
        




