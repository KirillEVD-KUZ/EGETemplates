mxX=0
for x in range(1,1500):
    ch=""
    x1=x
    while x1>0:
        ch+=str(x1%4)
        x1//=4
    ch=ch[::-1]
    if x%4==0:
        ch="2"+ch+"03"
    if x%4!=0:
        ost=(x%4)*5
        ch_ost=""
        while ost>0:
            ch_ost+=str(ost%4)
            ost//=4
        ch_ost=ch_ost[::-1]
        ch=ch+ch_ost
    res=int(ch,4)
    print(x,res)
    if res<=567 and mxX<x:
        mxX=x
print()
print(mxX)
