a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
while a > b:
    r = a
    a = b
    b = r
    continue
while b > c:
    r = b
    b = c
    c = r
    continue
while a > b:
    r = a
    a = b
    b = r
    continue
while x > y:
    r = x
    x = y
    y = r
    continue
if a < x and b < y:
    print ('Пройдет')
else:
    print('Не пройдет')
