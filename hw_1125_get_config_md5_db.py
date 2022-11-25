from function_ssh_get_gw import qytang_ssh
import sqlite3
import hashlib
import time
def get_md5(get_config):
    m = hashlib.md5()
    m.update(get_config.encode())
    return m.hexdigest()
# print(get_md5(get_config))
def update_config():
    conn = sqlite3.connect("qytang_confige_1125.sqlite")
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE config_md5 SET config = '{get_config}', md5 ='{get_md5(get_config)}' WHERE ip ='{ipadd}'")
    conn.commit()
    return
def insert_config():
    conn = sqlite3.connect("qytang_confige_1125.sqlite")
    cursor = conn.cursor()
    # cursor.execute("create table config_md5(ip varchar(40), config varchar(99999),md5 config varchar(999))")
    cursor.execute(f"insert into config_md5(ip,config,md5) values('{ipadd}','{get_config}','{get_md5(get_config)}')")  # 正常
    # # cursor.execute(("drop table config_md5"))
    cursor.execute("select * from config_md5")
    result = cursor.fetchall()
    conn.commit()
    return
def seeall():
    conn = sqlite3.connect("qytang_confige_1125.sqlite")
    cursor = conn.cursor()
    cursor.execute("select * from config_md5")
    result = cursor.fetchall()
    conn.commit()
    for i in result:
        print(i)
def select_md5():
    conn = sqlite3.connect("qytang_confige_1125.sqlite")
    cursor = conn.cursor()
    cursor.execute(f"select md5 from config_md5 where ip ='{ipadd}'")
    result = cursor.fetchall()[0][0]
    return result

if __name__=='__main__':
    ipadd = '44.208.74.27'
    username = 'cisco'
    password = 'Cisc0123'
    while True:
        get_config = qytang_ssh(ipadd, username, password, cmd='show run | begin hostname')
        try :
            select_md5()
        except IndexError:
            print(f'数据库中没有此{ipadd}配置，开始写入数据库！')
            insert_config()
            print('写入完成！')
        now_md5 = get_md5(get_config)
        db_md5 = select_md5()
        if now_md5 == db_md5:
            print(f'IP: {ipadd}  md5: {now_md5}')
        else:
            update_config()
            print(f'md5 变化为 {now_md5}   数据库已更新！\n')
        time.sleep(5)
