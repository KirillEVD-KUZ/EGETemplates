x = 36**8 + 6**20 - 12
s = ''
while x != 0:
    s += str(x % 6)
    x //= 6
print(s.count("5"))