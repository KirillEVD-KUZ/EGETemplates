from itertools import product
count = 1
for p in product("АПРСУ", repeat = 4):
    if "А" not in p:
        break
    count +=1
print(count)
