import paramiko
def qytang_ssh(ip,username,password,port=22,cmd='ls'):
    # ip = '18.166.73.48'
    # username='root'
    # password='woshiboshiqian'
    # cmd ='ls'
    ssh = paramiko.SSHClient()
    # ssh.load_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port=22,username=username,password=password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

if __name__=='__main__':
    print(qytang_ssh('18.166.73.48','root','woshiboshiqian'))
    print(qytang_ssh('18.166.73.48','root','woshiboshiqian',cmd='pwd'))
    print(qytang_ssh('18.166.73.48','root','woshiboshiqian', cmd='ip route'))
