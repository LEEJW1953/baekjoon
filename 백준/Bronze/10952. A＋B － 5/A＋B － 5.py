n=1
while 0<n:
    a,b=map(int, input().split())
    if a!=0:
        print(a+b)
        n=a+b
    else:
        break