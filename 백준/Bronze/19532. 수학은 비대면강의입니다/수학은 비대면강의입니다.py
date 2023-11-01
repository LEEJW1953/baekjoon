import sys
input=sys.stdin.readline

a,b,c,d,e,f=map(int,input().split())
for i in range(-999, 1000):
    for j in range(-999, 1000):
        x=a*i+b*j
        if x==c:
            y=d*i+e*j
            if y==f:
                print(i, j)
                exit(0)