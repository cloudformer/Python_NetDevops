import sys
import hashlib
def qytang_get_config(ip,username,password):
    from function_ssh_get_gw import qytang_ssh
    csr_config = qytang_ssh(ip,username,password,port=22,cmd='show run | begin hostname')
    return csr_config
if __name__=='__main__':
    print(qytang_get_config('44.208.74.27','cisco','Cisc0123'))
