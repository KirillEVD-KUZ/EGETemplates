from ipaddress import*
for m in range(33):
    ip=ip_network(f"222.190.122.24/{m}",0)
    if ip.network_address == ip_address('222.190.120.0'):
        print(ip.num_addresses)