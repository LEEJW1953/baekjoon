import sys
input=sys.stdin.readline

n=int(input())
red=[]
gre=[]
blu=[]
a, b, c=map(int, input().split())
rr=a
gg=b
bb=c
red.append(a)
gre.append(b)
blu.append(c)
for i in range(n-1):
    a, b, c=map(int, input().split())
    red.append(a)
    gre.append(b)
    blu.append(c)
    rr1=a+min(gg, bb)
    gg1=b+min(rr, bb)
    bb1=c+min(rr, gg)
    rr=rr1
    gg=gg1
    bb=bb1
result=min(rr, gg, bb)
print(result)