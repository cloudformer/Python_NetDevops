# -*- coding: utf-8 -*-import os
from ping_class_1 import QYTPING
from kamene.all import *
class QYTPING_NEW(QYTPING):
    def __init__(self,dstip,srcip='172.20.10.7',size=300):
        self.size = size
        self.dstip = dstip
        self.srcip = srcip
    def five(self):
        five_show = []
        ping_pkt = IP(dst=self.dstip) / ICMP()
        ping_result = sr1(ping_pkt, timeout=2, verbose=False)
        for i in range(5):
            if ping_result:
                five_show.append('+')
            else:
                five_show.append('?')
        return print(''.join(five_show))
    def __str__(self):
        return f'<{self.__class__.__name__} => dstip: {self.dstip}, size: {self.size}'
    # def five(self):
    #     if QYTPING_NEW(dstip).reply_value
if __name__ =="__main__":
    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s*int((70-len(word))/2),word,s*int((70-len(word))/2)))
    ping = QYTPING('1.1.1.1')
    newping = QYTPING_NEW('8.8.8.8')
    total_len = 70


    print_new('print class')
    print(ping)
    print_new('ping one for sure reachable')
    ping.one()
    print_new('ping five')
    ping.five()
    print_new('set payload lenth')
    ping.size=200
    print(ping)
    ping.five()
    print_new('set ping src ip address')
    ping.srcip='192.168.1.1'
    print(ping)
    ping.five()
    print_new('new class NewPing','=')
    print(newping)
    newping.five()
