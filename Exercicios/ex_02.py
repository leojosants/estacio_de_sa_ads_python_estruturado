a = 0

for i in range(30):         
    if (a % 2 == 0):
        a += 1
        continue
    else:
        if (a % 5 == 0):
            break
        else:
            a += 3

print(a)

"""
    0/29    a=0     if-->a%2(0%0=0) V       a+=1(0+1=1)     a=1
    1/29    a=1     if-->a%2(1%2=1) f       else-->         a=1     if-->a%5(1%5=0) f       else-->a+=3(1+3=4)
    2/29    a=4     if-->a%2(4%2=0) v       a+=1(4+1=5)     a=5
    3/29    a=5     if-->a%2(5%2=1) f       else-->         a=5     if-->a%5(5%5=0) v   break

"""