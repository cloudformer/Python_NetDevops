list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]
# for j in list1:
#     if (j in list2):
#         print(f'{j} in List1 and List2')
#     else:
#         print(f'{j} only in List1')
x=lambda list2,j: True if j in list2 else False
for j in list1:
    if (x(list2,j)):
        print(f'{j} in List1 and List2')
    else:
        print(f'{j} only in List1')
