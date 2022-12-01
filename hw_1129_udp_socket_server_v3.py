import socket
import struct
import hashlib
import pickle
import sys
import datetime
def get_md5(str):
    m = hashlib.md5()
    m.update(str.encode())
    return m.digest()
address = ('0.0.0.0',6666)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(address)
# obj = []
dayin = '{:<15}: {:<15}'
print('UDP服务器就绪！等待客户端发送数据！')
while True:
    try:
        aa = s.recvfrom(2048)
        msg, addr = aa
        obj = pickle.loads(msg)
        if obj == None:
            print('数据已传输完成，退出中...')
            break
        udp_head = struct.unpack('>hhlq',obj[0])
        if get_md5(str(obj[1])) != obj[2]:
            print('校验错误！')
            continue
        print('=' * 60)
        print('数据来源为          : IP：', addr[0],'端口:',addr[1])
        print(dayin.format('数据序列号', udp_head[2]))
        print(dayin.format('数据长度为', udp_head[3]))
        print('数据内容为          :', pickle.loads(obj[1]))
    except KeyboardInterrupt:
        sys.exit()
s.close()

# print(f'接收数据msg:{msg}， 源地址：{addr}')
# print(f'收到数据，序列：{udp_head[2]}')
# print(f'得到数据后校验： {get_md5(str(obj[1]))}')
# print(f'传输前的校验值： {obj[2]}')
# # udp_head = struct.pack('>hhlq', version, pkt_type, seq_id, len(data))
# print(udp_head[0],udp_head[1],udp_head[2],udp_head[3])
# print(f'数据内容:  {pickle.loads(obj[1])}')
# print(f'打印长度：{udp_head[3]}')
# print(obj[1])
