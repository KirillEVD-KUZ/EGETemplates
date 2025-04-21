
mx0=0
mxz=0
for x in range(1,2031):
    a=7**170+7**100-x
    sm=""
    a1=a
    while a1>0:
        sm+=str(a1%7)
        a1//=7
    if sm.count("0")>=mx0:
        mx0=sm.count("0")
        mxz=x
    print(mxz,mx0)