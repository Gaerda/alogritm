q = float(input())
s = 0
i = 1
while True:
    s = s + i
    i = i + 1
    if not s <= q:
        print (s, '>', q)
        break
print (i - 2)
