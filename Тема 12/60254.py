for i in range(3,10001,):
    a="5" + ("2"*i)
    while "52" in a or "2222" in a or "1122" in a:
        if "52" in a:
            a=a.replace("52", "11", 1)
        if "2222" in a:
            a=a.replace("2222", "5", 1)
        if "1122" in a:
            a=a.replace("1122", "25, 1")
    if a.count("5") * 5 + a.count("1") + a.count("2") *2 == 64:
        print(i)