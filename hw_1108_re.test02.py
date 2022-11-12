import re
str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
res = re.match('(\w{3,4})\s\S+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,5})\s\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,5}).\s[a-z]+\s(\d{1,2}).(\d{1,2}).(\d{1,2}).\s\w+\s(\d+).\s\w+\s(\w+)',str).groups()
print(f'protocol       :{res[0]}')
print(f'server         :{res[1]}')
print(f'localserver    :{res[2]}')
print(f'idle           :{res[3]} 小时 {res[4]}分钟 {res[5]}秒')
print(f'bytes          :{res[6]}')
print(f'flags          :{res[7]}')
