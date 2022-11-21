import paramiko
import time
import sys
def ssh_shell(ip,username,password,cmd_list,port=22,enable='',wait_time=1,verbose=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,username=username,password=password,port=port,timeout=5,compress=True)
    chan = ssh.invoke_shell()
    # stdin,stdout,stderr = ssh.exec_command(cmd)
    # x = stdout.read().decode()
    # while True:
    # for cmd in cmd_list:

    while True:
        x = chan.recv(2048).decode()
        if verbose==True:
            print(x,end='')
        cmd = input()
        if cmd == 'exit':
            break
        chan.send(cmd+'\n')
        time.sleep(wait_time)
    return
# def qytang_multicmd(ip,username,password,cmd_list):
#     from function_ssh_get_gw import qytang_ssh
#     for cmd in cmd_list:
#         res = qytang_ssh(ip,username,password,port=22,cmd=cmd)
#         print(res)
#     return

cmd_list=[
'config t',
'hostname aa',
'show version',
]
# qytang_multicmd('44.208.74.27',username='cisco',password='Cisc0123',cmd_list=cmd_list)
ssh_shell('44.208.74.27',username='cisco',password='Cisc0123',cmd_list=cmd_list,wait_time=2, verbose=True)

