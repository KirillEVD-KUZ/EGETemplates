mx=0
mk=0
for x in range(0,2031):
    a = (3 ** 100) - x
    a1=a
    tr = ""
    while a1 >0:
        tr+=str(a1%3)
        a1//=3
    if tr.count("0") > mx:
        mx=tr.count("0")
        res=int(str(mx),3)
print(res)
