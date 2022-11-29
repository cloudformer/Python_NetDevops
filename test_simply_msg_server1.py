import socket
import struct
import hashlib
import pickle
import sys

address = ('0.0.0.0',6666)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(address)

print('UDP服务器就绪！等待客户端发送数据！')
while True:
    try:
        aa = s.recvfrom(2048)
        print(aa)
        data, addr = aa
        if not data:
            print('数据为空，退出中...')
            break
        print(f'接收数据，{data}， 源地址：{addr}')
    except KeyboardInterrupt:
        sys.exit()
s.close()
