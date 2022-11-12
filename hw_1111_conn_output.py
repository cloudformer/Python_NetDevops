import re
asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
asa_dict={}
conn = re.split('\n',asa_conn)
for i in range(0,len(conn)):
    re_result = re.match("[\s\S]+\s+\S+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:(\d{1,5})\s\S+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:(\d{1,5})\,\sidle\s\d{1,2}\:\d{1,2}\:\d{1,2}\,\sbytes\s(\d{1,6})\,\sflags\s(\w{1,3})",conn[i]).groups()  asa_dict[re_result[0],re_result[1],re_result[2],re_result[3]]=re_result[4],re_result[5]
format_str1 = "src_ip :{:<15}| src   :{:^10}|  dst_ip :{:<15} |  dst :{:^10}"
format_str2 = "bytes  :{:^15}| flags :{:^10}"
format_str3 = '='*85
print(f'打印分析后的字典！\n{asa_dict}\n')
print('格式化打印输出\n')
for key,value in asa_dict.items():
    print(format_str1.format(key[0],key[1],key[2],key[3]))
    print(format_str2.format(value[0],value[1]))
    print(format_str3)
