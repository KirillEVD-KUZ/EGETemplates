def f(s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '30', 1)
        s = s.replace('02', '101', 1)
        s = s.replace('03', '202', 1)
    return s


for x1 in range(80):
    for x2 in range(80):
        for x3 in range(80):
            line = '0' + '1' * x1 + '2' * x2 + '3' * x3
            res = f(line)
            if res.count('1') == 15 and res.count('2') == 10 and res.count('3') == 60:
                print(x1)
