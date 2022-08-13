n=int(input())
a=n//5
b=n-a*5
for i in range(a+1):
    if a==0 and b%3!=0:
        print(-1)
    elif b%3==0:
        print(a+b//3)
        break
    else:
        a-=1
        b+=5