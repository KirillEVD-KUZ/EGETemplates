for x in "01234567":
    a=int(f"{x}1{x}",16)
    b=int(f"{x}3{x}3",8)
    print(x,a+b)