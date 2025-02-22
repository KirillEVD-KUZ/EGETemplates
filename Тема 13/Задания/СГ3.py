from ipaddress import ip_network

ip = '68.30.20.77'
# Кол-во единиц в host == кол-ву нулей в mask
net = None
for mask in range(33):
    net = ip_network(f'{ip}/{mask}', strict=False)
    if f'{net.network_address:b}'.count('1') == f'{net.netmask:b}'.count('0'):
        break
count = 0
for ip in net:
    if f'{ip:b}'.count('1') == 10:
        count += 1
print(count)




