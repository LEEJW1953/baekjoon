import sys
input=sys.stdin.readline

def f(tmp):
    if sum(vis)==k:
        if tmp not in d:
            d[tmp]=1
        return
    for i in range(n):
        if not vis[i]:
            vis[i]=1
            f(tmp+arr[i])
            vis[i]=0

n=int(input())
k=int(input())
arr=[input().strip() for _ in range(n)]
vis=[0]*n
d={}
f('')
print(len(d.values()))