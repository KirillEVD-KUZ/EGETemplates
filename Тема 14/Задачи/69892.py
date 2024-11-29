res=(3 * (289**2024)) + (81 * (49 **121)) - (9 * (16 **81)) - 6011
sum = 0
while res>0:
    num= res % 31
    if num <= 17:
        sum+=num
    res = res // 31
print(sum)