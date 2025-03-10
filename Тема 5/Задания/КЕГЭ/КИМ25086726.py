for x in range(13):
    b=bin(x)[2:]
    if x%2==0:
        b="10"+b
    if x%2!=0:
        b="1"+b+"01"
    res=int(b,2)
    print(x,res,b)