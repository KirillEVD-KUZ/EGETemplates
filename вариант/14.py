for a in range(1, 100000):
    ch = 3 ** 10 + 3 ** 7 + 3 ** 3 + 2 - a
    tr=""
    while ch>0:
        tr+=str(ch%3)
        ch//=3
    tr=tr[::-1]
    if tr.count("0")==tr.count("1")==tr.count("2"):
        print(a)