import sys
input=sys.stdin.readline

def dis1(n, m):
    result=(((n-x)**2+(m-(y+r))**2)**0.5)
    return result
def dis2(n, m):
    result=(((n-(x+w))**2+(m-(y+r))**2)**0.5)
    return result

w, h, x, y, p=map(int, input().split())
r=h//2
count=0
for i in range(p):
    xx, yy=map(int, input().split())
    if (x<=xx) and (xx<=(x+w)):
        if (y<=yy) and (yy<=(y+h)):
            count+=1
    elif ((x-r)<=xx) and (xx<x):
        if (y<=yy) and (yy<=(y+h)):
            if dis1(xx, yy)<=r:
                count+=1
    elif (x+w)<xx and xx<=(x+w+r):
        if y<=yy and yy<=(y+h):
            if dis2(xx, yy)<=r:
                count+=1
print(count)