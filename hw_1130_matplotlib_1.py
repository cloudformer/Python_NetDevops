
import matplotlib
a = matplotlib.matplotlib_fname()
print(f'路径： {a}')
from matplotlib import pyplot as plt
def mat_bing(name_list,cont_list,bing_name):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(6,6))
    patches,l_text,p_text = plt.pie(cont_list,
                                    labels=name_list,
                                    labeldistance=1.1,
                                    autopct='%3.1f%%',
                                    shadow=False,
                                    startangle=90,
                                    pctdistance=0.6)
    for t in l_text:
        t.set_size = 30
    for t in p_text:
        t.set_size = 30
    plt.axis('equal')
    plt.title(bing_name)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    import re
    mat_bing(['名称1','名称2','名称3'],[1000,123,444],'第三天作业Netflow')
    # from function_ssh_get_gw import qytang_ssh
    # flow_show = qytang_ssh('44.208.74.27','cisco','Cisc0123',port=22,cmd='show flow monitor name qytang-monitor cache format table')
    # # print(flow_data)
    # flow_data = flow_show.split('  ==========\r\n')
    # print(flow_data[1])
    # data = flow_data[1].split('\n')
    # # data = ['port ssh                                4930\r',
    # #         'layer7 ping                               40\r',
    # #        'telnet                                  2230\r',
    # #         '']
    # raw = len(data) - 1
    # name_list= []
    # num_list=[]
    # for i in range(0,raw):
    #     # a = re.match('(\w\s)\s+(\d{1,10})',data[raw]).groups()
    #     a = re.match('([a-z0-9\s]{1,12})\s+(\d{1,10})',data[i]).groups()
    #     name_list.append(a[0])
    #     num_list.append(a[1])
    # print(name_list,num_list)
    # mat_bing(name_list, num_list, '第三天作业Netflow')
