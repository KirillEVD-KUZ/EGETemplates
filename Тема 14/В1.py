cl0=0
x1=0
for x in range(0, 2031):
    a = 3 ** 100 - x
    a1=a
    tr=""
    while a1>0:
        tr+=str(a1%3)
        a//=3
    if cl0>tr.count("0"):
        cl0=tr.count("0")
        x1=x
print(x1, cl0)