a = int(input())
b = int(input())
c = (c:=a, a:=b, b:=c)
print (a, b)
