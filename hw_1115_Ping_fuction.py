#-*- coding: utf-8 -*-import os
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *
import os
def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return '!'
    else:
        return '.'
if __name__== '__main__':
    ip = input("What IP you want to reach?: ")
    result = qytang_ping(ip)
    if result == '!':
        print(f'{ip} 通')
    else:
        print(f'{ip} 不通')
