import socket
import struct
import pickle
import hashlib
import time
from datetime import datetime
def get_md5(str):
    m = hashlib.md5()
    m.update(str.encode())
    return m.digest()
def udp_send_data(faddress,fdata):
    address = faddress
    data_list = fdata
    version = 1
    pkt_type = 1
    seq_id = 1
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    for data in data_list:
        data1 = pickle.dumps(data)
        udp_head = struct.pack('>hhlq', version, pkt_type, seq_id, len(str(data)))
        packet = [udp_head, data1, get_md5(str(data1))]
        # packet = [udp_head, data, get_md5(data)]         #错误
        msg = pickle.dumps(packet)
        print(f'序列{seq_id} : {data}\n内容已发送！')
        if len(data_list) == seq_id:
            s.sendto(msg,address)
            packet = None
            msg = pickle.dumps(packet)
            s.sendto(msg,address)
            break
        s.sendto(msg,address)
        time.sleep(1)
        seq_id += 1
    s.close()
if __name__ == '__main__':
    address = ('127.0.0.1', 6666)
    data_list = ['hello udp',['世界你好','好好学习'],{'姓名':'王五', '年龄':'33'},{'time':datetime.now()}]
    udp_send_data(address,data_list)
