"""ip = '135.21.171.214'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
print()
ip = '255.255.248.0'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))"""
b=input()
bin=int(b,2)
print(bin)
