t=int(input())
for i in range(t):
    h,w,n=map(int, input().split())
    a=n%h
    b=(n-1)//h+1
    if a==0:
        a=h
    print(100*a+b)