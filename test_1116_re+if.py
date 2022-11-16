import re
line = '010-12345'
if re.match('^\d{3}\-\d{5,8}$',line):
    print('match!')
else:
    print('failed')
