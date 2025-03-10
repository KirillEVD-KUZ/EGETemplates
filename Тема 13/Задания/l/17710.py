from ipaddress import*
st=ip_network("214.187.224.0/255.255.224.0",0)
k=0
for ip in st:
    b=bin(int(ip))[2:].zfill(32)
    if b.count("1")%6!=0 and b[:4]=="1000":
        k+=1
print(k)
#17710
