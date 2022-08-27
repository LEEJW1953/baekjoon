import sys

t=int(sys.stdin.readline())
for i in range(t):
    count=0
    x1, y1, x2, y2=map(int, sys.stdin.readline().split())
    n=int(input())
    for j in range(n):
        cx, cy, r=map(int, sys.stdin.readline().split())
        d1=((x1-cx)**2+(y1-cy)**2)**0.5
        d2=((x2-cx)**2+(y2-cy)**2)**0.5
        if d1<r and r<d2:
            count+=1
        elif d2<r and r<d1:
            count+=1
    print(count)