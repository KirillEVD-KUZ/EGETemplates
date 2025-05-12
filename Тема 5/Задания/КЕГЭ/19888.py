mx=0
for x in range(1,100000):
    x1=x
    vs=""
    while x1>0:
        vs+=str(x1%8)
        x1//=8
    if x%2==0:
        vs=vs.replace("1","2").replace("3","2").replace("5","2").replace("7","2")
    if x%2!=0:
        vs="3"+vs[1:]
        vs=vs[:-1]+"3"
    vs1=vs[::-1]
    res=int(vs1,8)
    if res>mx and res<300:
        mx=res
print(mx)