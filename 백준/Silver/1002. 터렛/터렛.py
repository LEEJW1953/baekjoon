import sys
t=int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    dis=((x1-x2)**2+(y1-y2)**2)**0.5
    if x1!=x2 or y1!=y2:
        if r1+r2>dis:
            if abs(r1-r2)==dis:
                print(1)
            elif abs(r1-r2)<dis:
                print(2)
            elif abs(r1-r2)>dis:
                print(0)
        elif r1+r2<dis:
            print(0)
        elif r1+r2==dis:
            print(1)
    elif x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)