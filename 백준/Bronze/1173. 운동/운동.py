import sys
input=sys.stdin.readline

n, m, M, t, r = map(int, input().split())
x=m
total=0
move=0
if m+t>M:
    print(-1)
    exit(0)
if n==0:
    print(n)
    exit(0)
while move<n:
    if x+t<=M:
        total+=1
        move+=1
        x+=t
    else:
        total+=1
        x-=r
        if x<m:
            x=m
print(total)