department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456
#字符串格式化 传统技术
line1='Department name:%-9s Manager:%-8s COURSE FEES:%-10.2f THE END!'%(department1,depart1_m,COURSE_FEES_SEC)
line2='Department name:%-9s Manager:%-8s COURSE FEES:%-10.2f THE END!'%(department2,depart2_m,COURSE_FEES_Python)
#字符串格式化 新方法
line3='Department name:{:<9} Manager:{:<8} COURSE FEES:{:<10.2f} The End!'.format(department1,depart1_m,COURSE_FEES_SEC)
line4='Department name:{:<9} Manager:{:<8} COURSE FEES:{:<10.2f} The End!'.format(department2,depart2_m,COURSE_FEES_Python)
length = len(line1)
firstline = '=' * length
endline = '-' * length
print(f'{firstline}\n{line1}\n{line2}\n{endline}')
print(f'{firstline}\n{line3}\n{line4}\n{endline}')
