import cmath 
a = float(input())
b = float(input())
c = float(input())
D = (b ** 2 - 4 * a * c)
if (D>=0):
    x1 = (-b - cmath.sqrt (D)) / (2 * a)
    x2 = (-b + cmath.sqrt (D)) / (2 * a)
    print (x1, x2)
else:
    print ('Решения нет')
