import random
win_times = 0
for i in range(100):
    a = random.randint(1, 100)
    b = random.randint(90, 100)
    if a>b:
        print('congratulations your win!')
        print(a, b)
        win +=1
    else:
        print('your lose!')
        # print(a,b)
print(f'You win this Game for {win_times} times!!!')
