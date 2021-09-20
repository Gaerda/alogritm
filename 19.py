st = int(input())
if st < 5:
    zp = 130
    print (zp)
elif st <= 15:
    zp = 180
    print (zp)
else:
    zp = 180 + (st - 15) * 10
    print (zp)
    
