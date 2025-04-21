from ipaddress import*
for a in range(256):
    net=ip_network(f"192.214.{a}.184/255.255.255.224",0)
    f=1
    for ip in net:
        b=bin(int(ip))[2:]
        if b.count("1")<=15:
            f=0
            break
    if f==1:
        print(a)
        break