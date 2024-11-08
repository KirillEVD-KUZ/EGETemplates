import itertools
list_values= itertools.product("ЕИМНРТ", repeat =10)
count = 0
num=1
for str in list_values:
    line="".join(str)
    if (num % 3 == 0) and (line[0] == "И" or line[0] == "Е") and (line.count("Т") == 1):
        count +=1
    num +=1
print(count)