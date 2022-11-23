# -*- coding: utf-8 -*-import os
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *
import os
class QYTPING:
    def __init__(self, dstip,srcip='172.20.10.7',size=100):
        self.dstip = dstip
        self.srcip = srcip
        self.size = size
    def reply_value(self):
        pkt_payload = '=' * self.size
        ping_pkt = IP(src=self.srcip,dst=self.dstip) / ICMP()/pkt_payload
        ping_result1 = sr1(ping_pkt, timeout=2, verbose=False)
        if ping_result1:
            return ping_result1.show
    def one(self):
        if self.reply_value():
            return print(f'{self.dstip} 可达！')
        else:
            return print(f'{self.dstip} 不可达！')
    def five(self):
        five_show = []
        for i in range(5):
            if self.reply_value():
                five_show.append('!')
            else:
                five_show.append('.')
        return print(''.join(five_show))
    # def length(self,size):
    #     self.size = size
    def __str__(self):
        if self.srcip=='172.20.10.7':
            return f'<{self.__class__.__name__} => dstip: {self.dstip}, size: {self.size}'
        else:
            return f'<{self.__class__.__name__} => srcip: {self.srcip}, dstip: {self.dstip}, size: {self.size}'

if __name__ =="__main__":

    # def print_new(word, s='-'):
    #     print('{0}{1}{2}'.format(s*int((70-len(word))/2),word,s*int((70-len(word))/2)))
    ping = QYTPING('8.8.8.8')
    total_len = 70
    print(ping.reply_value())
