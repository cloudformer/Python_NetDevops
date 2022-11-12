import re
port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34',\
             'eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
res_list =[]
port_sorted_format = '{}/{}/{}'
sorted_list=[]
for i in range(0,len(port_list)):
    res = re.match('(eth\s+\d\/\d{1,3})\/(\d{1,3})\/(\d{1,3})', port_list[i]).groups()
    res_list.append(res)
    res1_list = sorted(res_list,key=lambda x: (int(x[1]),int(x[2])))
for i in range(0,len(port_list)):
    sor = res1_list[i]                
sorted_list.append(port_sorted_format.format(sor[0],sor[1],sor[2]))
print(sorted_list)
