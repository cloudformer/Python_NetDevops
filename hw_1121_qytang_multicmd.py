import paramiko
import time
import threading
import sys
def qytang_multicmd(ip,username,password,cmd_list,port=22,enable='',wait_time=1,verbose=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,username=username,password=password,port=port,timeout=5,compress=True)
    chan = ssh.invoke_shell()
    for cmd in cmd_list:
        resp = chan.recv(2048).decode()
        if verbose==True:
            print(resp,end='')
        if enable !='':
            chan.send('en'+'\n')
            chan.send(enable+'\n')
            print(chan.recv(2048).decode())
        chan.send(cmd+'\n')
        time.sleep(wait_time)
    return

cmd_list=[
'terminal length 512',
'show version',
'config t',
'interface GigabitEthernet1',
'ip ospf network point-to-point',
'ip ospf multi-area 99',
'ip ospf 1 area 0',
'end',
'show ip ospf 1',
'hostname bb'
]
# qytang_multicmd('44.208.74.27',username='cisco',password='Cisc0123',enable='en',cmd_list=cmd_list)
qytang_multicmd('44.208.74.27',username='cisco',password='Cisc0123',cmd_list=cmd_list,wait_time=2, verbose=True)

