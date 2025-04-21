for x in "0123456789ABCDEFGHIGKLM":
    a=int(f"98{x}79641",22)
    b=int(f"25{x}49",22)
    c=int(f"63{x}5",22)
    if (a+b+c)%21==0:
        print((a+b+c)//21)