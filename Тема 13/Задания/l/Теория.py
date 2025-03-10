# Известен IP и Mask
from ipaddress import ip_network, ip_address

# Адрес сети
n.network_adress

# Маска не известна
for m in range(33):
    n=ip_network(f"ip/{m}",0)

# Маска
n.netmask #n-имя сети

#Кол-во адресов сети
n.num_addresses

#формат адреса
ip_address

#ip в 2сс
b=f"{ip:b}"
or
b=bin(int(ip))[2:].zfill(32)
