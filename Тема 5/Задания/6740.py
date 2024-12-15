for i in range(1,9):
    b=bin(i)[2:]
    if i %2 ==0:
        b="10" + b
    else:
        b= "1" + b  +"01"
    isk=int(b,2)
    print(i, isk)
#61