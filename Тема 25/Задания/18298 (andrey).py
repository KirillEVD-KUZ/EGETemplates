import re

for i in range(0, 10 ** 10, 1996):
    if re.fullmatch(r"1592[2468]*6\d8", str(i)):
        print(i, i // 1996)
