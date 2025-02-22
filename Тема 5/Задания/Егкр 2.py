for x in range (1, 10000000000):
    tr= ""
    n= x
    while n>0:
        tr+=str(n % 3)
        n=n//3
    tr=tr[::-1]
    tr=tr.replace("0", "*")
    tr=tr.replace("2", "0")
    tr=tr.replace("*", "2")
    tr=tr.lstrip("0") or "0"
    res=int(tr,3)
    res1=abs(x-res)
    if res1 == 1824648:
        print(x)
