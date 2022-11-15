import os
import re
import time
cmd = 'netstat -tulnp'
a = []
# print(a)     #('tcp', '111')
while a==[]:
    str = os.popen(cmd).read()
    a = re.findall('[\s\S](tcp)\s+\S\s+\S\s0.0.0.0:(80)\s', str)
    print('等待一秒重新开始监控！')
    time.sleep(1)
    if a==[('tcp', '80')]:
        print(f'HTTP({a[0][0]}/{a[0][1]})服务已经被打开！')
 #       break

#############################################  另一个进程启动 80 服务
# #!/usr/bin/python3.6
# # -*- coding=utf-8 -*-
# from http.server import HTTPServer, CGIHTTPRequestHandler
# port = 80
# httpd = HTTPServer(('',port), CGIHTTPRequestHandler)
# print('Starting simple httpd on port: ' + str(httpd.server_port))
