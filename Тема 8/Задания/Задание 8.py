import itertools
list_values = itertools.product('ГЕПАРД', repeat = 5)
count = 0
for str in list_values:
    line = ''.join(str)
    if line.count("Г") == 1 and line[0] !="А" and line[-1] !="Е":
        count += 1
print(count)