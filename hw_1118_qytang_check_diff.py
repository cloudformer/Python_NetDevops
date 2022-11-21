import sys
import hashlib
import time
def qytang_get_config(ip,username,password):
    from function_ssh_get_gw import qytang_ssh
    csr_config = qytang_ssh(ip,username,password,port=22,cmd='show run | begin hostname')
    return csr_config
def qytang_check_diff(ip,username,password):
    res_md5 = ''
    while True:
        configfile = qytang_get_config(ip, username, password)
        m = hashlib.md5()
        m.update(configfile.encode())
        if res_md5 =='':
            res_md5 = m.hexdigest()
        if res_md5 == m.hexdigest():
            print(f'{res_md5}')
        else:
            print(m.hexdigest())
            print(f'MD5 value changed!')
            break
        time.sleep(2)
    return res_md5
if __name__=='__main__':
    qytang_check_diff('44.208.74.27','cisco','Cisc0123')
