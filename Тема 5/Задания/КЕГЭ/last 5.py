maks=0
for i in range(1, 1000):
    n = i
    vs = ""
    while n > 0:
        vs += str(n % 8)
        n //= 8
    vs=vs[::-1]
    if i % 2 == 0:
        vs = vs.replace("1", "2")
        vs = vs.replace("3", "2")
        vs = vs.replace("5", "2")
        vs = vs.replace("7", "2")
    if i % 2 != 0:
        vs="3" + vs[1:]
        vs=vs[:1] + "3"
    res= int(vs, 8)
    if res<300:
        if res>maks:
            maks=res
print(maks)