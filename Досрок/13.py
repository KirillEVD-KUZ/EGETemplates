from ipaddress import*
ip=ip_network("143.168.72.208/255.255.255.240",0)
for m in ip:
    print(m)

#14316872222