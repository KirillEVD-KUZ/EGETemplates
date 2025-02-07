found_num=set()
chisl = 0
for i in range (500000, 600000):
    for y in range (18,5000):
        if i % y == 0 and y%10==8:
           if i not in found_num:
               found_num.add(i)
               chisl +=1
               print(i, y)
        if chisl>5:
            break
    if chisl>5:
        break