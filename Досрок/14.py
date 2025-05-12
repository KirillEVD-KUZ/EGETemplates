for x in "0123456789ABCDEFGHIJK":
    a = int(f"82934{x}2", 21)
    b = int(f"2924{x}{x}7", 21)
    c = int(f"67564{x}8", 21)
    sm=a+b+c
    if sm%20==0:
        print(sm//20)
