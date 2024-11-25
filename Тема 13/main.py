ip = '84.77.95.123'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
print()
ip = '84.77.96.123'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))