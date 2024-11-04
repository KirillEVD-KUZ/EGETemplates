chet = "0246"
nchet = "357"
count = 0

for n1 in nchet:
    for n2 in chet:
        for n3 in nchet:
            for n4 in chet:
                for n5 in nchet:
                    line = n1 + n2 + n3 + n4 + n5
                    if (line.count("0") <= 1 and line.count("2") <= 1 and line.count("3") <= 1 and line.count("4") <= 1 and line.count("5") <= 1 and line.count("6") <= 1 and line.count("7") <= 1) :
                        count +=1
print(count)
#108 + 72 =180