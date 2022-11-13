numbers = [12,37,4,2,66,74,77,43,99,3,64,90]
even=[]
odd=[]
# for loop
for number in numbers:
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)
# while loop
# while len(numbers)>0:
#     number = numbers.pop()
#     if number %2==0:
#         even.append(number)
#     else:
#         odd.append(number)
print(f'numbers:{numbers}')
print(f'even:{even}')
print(f'odd:{odd}')
