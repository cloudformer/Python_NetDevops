import os
# os.mkdir('test')
# print(os.getcwd())
# qytang1 = open('qytang1','w')
# qytang1.write('test file\n')
# qytang1.write('this is qytang1\n')
# qytang1.close()
# qytang2 = open('qytang2','w')
# qytang2.write('test file\n')
# qytang2.write('this is qytang2\n')
# qytang2.close()
# qytang3 = open('qytang3','w')
# qytang3.write('test file\n')
# qytang3.write('this is qytang3\n')
# qytang3.close()
# os.mkdir('qytang4')
# os.mkdir('qytang5')
os.chdir('test')
print(f'os.listdir()={os.listdir()}')
for i in os.listdir():
    if os.path.isfile(i):
        print(f'{i} is file!')
    else:
        print(f'{i} is folder!')
