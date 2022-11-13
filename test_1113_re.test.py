import re
c = re.match( 'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats')
print(c)
d = re.match( 'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats').groups()
print(d)
a = re.findall( 'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats')
print(a)
b = [x.group() for x in re.finditer( 'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats')]
print(b)
e = re.split(',','all cats are smarter than dogs, all dogs are dumber than cats')
print(e)

#result
# <re.Match object; span=(0, 12), match='all cats are'>
# ('cats',)
# ['cats', 'dogs']
# ['all cats are', 'all dogs are']
# ['all cats are smarter than dogs', ' all dogs are dumber than cats']
