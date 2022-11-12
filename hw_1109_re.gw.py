#!/usr/bin/python
#-*- coding: utf-8 -*-import os
import os
import re
ifconfig_result = os.popen('ifconfig ' + 'eth0').read()
ipv4_add = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[0]
netmask = re.findall('255\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[0]
broadcast = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.255',ifconfig_result)[0]
mac_addr = \
    re.findall('[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]\:[0-9a-f][0-9a-f]'
               ,ifconfig_result)[0]

format_string = "{:<12}: {}"
print(format_string.format(f'ipv4_add',ipv4_add))
print(format_string.format(f'netmask',netmask))
print(format_string.format(f'broadcast',broadcast))
print(format_string.format(f'mac_addr',mac_addr))
#产生网关,网段第一位,匹配ipv4地址前三位
net = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.)',ipv4_add)[0]
ipv4_gw = net + '1'
print('\n我们第一个可用IP地址为网关：' + ipv4_gw + '\n')
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()
re_ping_result =re.findall('\s(\d)\sreceived\,',ping_result)[0]
# print(re_ping_result)
if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')
