for x in range(1000, 10000):
    x = str(x)

    ch1 = int(x[:1])
    ch2 = int(x[1:][:1])
    ch3 = int(x[2:][:1])
    ch4 = int(x[3:])

    umn1=ch1*ch2
    umn2=ch1*ch3
    umn3=ch1*ch4

    mx=max(umn1,umn2,umn3)
    mn=min(umn1,umn2,umn3)
    md=(umn1+umn2+umn3)-mx-mn
    otv=f"{md}{mx}"
    if otv=="5472":
      print(x)


