#!/usr/bin/python
#-*- coding: utf-8 -*-import os
import os
import re
route_n_result = os.popen('route -n').read()
gw = re.findall('\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S+\s+UG',route_n_result)[0]
print(f'网关为：{gw}')
