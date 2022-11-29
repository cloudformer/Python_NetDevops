import socket
import struct
import hashlib
import pickle
address = ('172.20.10.7',6666)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg = input('请输入数据：')
    if not msg:
        s.sendto(msg.encode(),address)
        break
    s.sendto(msg.encode(),address)
s.close()
