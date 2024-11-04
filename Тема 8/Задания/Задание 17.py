chet = "2468"
nchet = "1357"
count = 0

for n1 in nchet:
    for n2 in chet:
        for n3 in nchet:
            for n4 in chet:
                for n5 in nchet:
                    for n6 in chet:
                        for n7 in nchet:
                            for n8 in chet:
                                for n9 in nchet:
                                    for n10 in chet:
                                        for n11 in nchet:
                                            line = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11
                                            if (line.count("1") <= 4 and line.count("2") <= 4 and line.count("3") <= 4 and line.count("4") <= 4 and line.count("5") <= 4 and line.count("6") <= 4 and line.count("7") <= 4 and line.count("8") <= 4):
                                                count +=1

chet = "2468"
nchet = "1357"
count1 = 0

for n1 in chet:
    for n2 in nchet:
        for n3 in chet:
            for n4 in nchet:
                for n5 in chet:
                    for n6 in nchet:
                        for n7 in chet:
                            for n8 in nchet:
                                for n9 in chet:
                                    for n10 in nchet:
                                        for n11 in chet:
                                            line = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11
                                            if (line.count("1") <= 4 and line.count("2") <= 4 and line.count("3") <= 4 and line.count("4") <= 4 and line.count("5") <= 4 and line.count("6") <= 4 and line.count("7") <= 4 and line.count("8") <= 4):
                                                count1 +=1
print(count + count1)