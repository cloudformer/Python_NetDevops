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
import paramiko
import re
def qytang_ssh(ip,username,password,port=22,cmd='ls'):
    ssh = paramiko.SSHClient()
    # ssh.load_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port=22,username=username,password=password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x
from pprint import pprint
def qytang_get_if(ips,username,password):
    print(f'ips={ips}')
    print(f'len={len(ips)}')
    iplist=[]
    # iplist.append(ips)
    iplist = ips
    device_if_dict = {}
    print(f'iplist={iplist}')
    for ip in iplist:
        # print(ip)
        result = qytang_ping(ip)
        if result == '!':
            show_all_interface = qytang_ssh(ip, username, password, cmd='show ip int brief')
            interface = {}
            show_line_interface = re.split('\n', show_all_interface)
            res = []
            for i in show_line_interface:
                res1 = re.match(r'([a-zA-Z]+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', i)
                if res1 != None:
                    interface[res1.groups()[0]] = res1.groups()[1]
            device_if_dict[ip] = interface
            print(f'{ip} 通')
        else:
            print(f'{ip} 不通')
            device_if_dict[ip] = {}
    pprint(device_if_dict)
    return device_if_dict
#
if __name__=='__main__':
    qytang_get_if(ips=('172.20.10.110','172.20.10.10','172.20.10.210'), username='cisco', password='Cisc0123')
    # qytang_get_if(ips=['54.210.75.14'], username='cisco', password='Cisc0123')
