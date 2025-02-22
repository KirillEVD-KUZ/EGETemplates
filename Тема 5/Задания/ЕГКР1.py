for x in range (1,100000000000):
    n=x
    tr=""

    while n > 0:
        tr+=str(n %3)
        n//=3
    tr=tr[::-1]
    tr=tr.replace("0", "*")
    tr=tr.replace("2", "0")
    tr=tr.replace("*", "2")
    tr=tr.lstrip("0") or "0"
    res=int(tr,3)
    res1=abs(x-res)
    if res1 == 1864246:
        print(x)
        break