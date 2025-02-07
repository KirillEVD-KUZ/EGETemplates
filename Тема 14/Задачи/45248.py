a=7 * (512 ** 1912) + 6 *(64**1954) - 5*(8 ** 1991) - 4 * (4 ** 1980) - 2022
ost=0
res=""
while a != 0:
    ost=a%8
    a=a//8
    res= res + f"{ost}"
otv=res.count("7")
print(otv)