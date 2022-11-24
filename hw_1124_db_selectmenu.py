import sqlite3
homework_dict = [{'姓名':'学员111','年龄':37,'作业数':1},
                 {'姓名':'学员222','年龄':33,'作业数':5},
                 {'姓名':'学员3','年龄':32,'作业数':10},]
str = "学员姓名:{:^5} 学员年龄:{:^5} 学员作业数:{:^5}"
# a = str.format(homework_dict[1]['姓名'],homework_dict[1]['年龄'] ,homework_dict[1]['作业数'])
conn = sqlite3.connect('homework1124.sqlite')
cursor = conn.cursor()
# cursor.execute("create table homework_info(姓名 varchar(40),年龄 int,作业数 int)")
# cursor.execute('insert into homework_info(姓名,年龄,作业数) values("学员1",37,1)')
# cursor.execute('insert into homework_info(姓名,年龄,作业数) values("学员2",33,5)')
# cursor.execute('insert into homework_info(姓名,年龄,作业数) values("学员3",32,10)')
# cursor.execute(("drop table homework_info"))
# cursor.execute("select * from homework_info")
# cursor.execute("select 姓名,作业数 from homework_info where 作业数 >3")
# result = cursor.fetchall()
# print(result)
# for i in result:
#     print(i)
# cursor.execute("create table homework_info(姓名 varchar(40),年龄 int,作业数 int)")
# for i in homework_dict:
#     name = i['姓名']
#     age =i['年龄']
#     num = i['作业数']
#     # print(name,age,num)
#     cursor.execute(f"insert into homework_info(姓名,年龄,作业数) values('{name}','{age}','{num}')")
# cursor.execute("select * from homework_info")
# result = cursor.fetchall()
# for i in result:
#     print(i)
# conn.commit()
def option1():
    cursor = conn.cursor()
    cursor.execute("select * from homework_info")
    result = cursor.fetchall()
    for i in result:
        print(str.format(i[0],i[1],i[2]))
    return
def option2():
    name = input('请输入要查询的姓名：')
    cursor = conn.cursor()
    cursor.execute(f"select * from homework_info where 姓名 == '{name}'")
    result = cursor.fetchall()
    if result == []:
        return print('学员信息未找到')
    for i in result:
        print(str.format(i[0],i[1],i[2]))
    return
def option3():
    age = input('搜索大于输入年龄的学员,请输入学员年龄：')
    cursor = conn.cursor()
    cursor.execute(f"select * from homework_info where 年龄 > '{age}'")
    result = cursor.fetchall()
    if result == []:
        return print('学员信息未找到')
    else:
        for i in result:
            print(str.format(i[0],i[1],i[2]))
    return
def option4():
    num = input('搜索大于输入作业数的学员,请输入作业数量：')
    cursor = conn.cursor()
    cursor.execute(f"select * from homework_info where 作业数 > '{num}'")
    result = cursor.fetchall()
    if result == []:
        return print('学员信息未找到')
    else:
        for i in result:
            print(str.format(i[0],i[1],i[2]))
    return
def option0():
    print('退出')
    return
user_notify = """
请输入查询选项：
输入1 ： 查询整个数据库
输入2 ： 基于姓名查询
输入3 ： 基于年龄查询
输入4 ： 基于作业数查询
输入0 ： 退出
"""
while True:
    print(user_notify)
    user_input = input('请选择：')
    if user_input == '0':
        break
    elif user_input == '1':
        option1()
    elif user_input == '2':
        option2()
    elif user_input == '3':
        option3()
    elif user_input == '4':
        option4()
    else:
        print('输入错误！请重试！')
