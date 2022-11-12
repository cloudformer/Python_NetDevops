import re
str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
res = re.match('(\d\d\d)\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\w{7})\s+([A-Z][a-z]\d\/\d\/\d\d)',str).groups()
print(f'VLAN ID    :{res[0]}')
print(f'MAC        :{res[1]}')
print(f'TYPE       :{res[2]}')
print(f'Interface  :{res[3]}')
