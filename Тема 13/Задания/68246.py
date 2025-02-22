"""ip = '147.222.199.75'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))"""
count = 0
for i in range(31):
    for j in range(256):
        ip = f'147.222.{192+i}.{j}' # Адрес сети host
        s = ' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')])
        if s.count('1') == 14 :
            count+=1
print(count)