import sys
input=sys.stdin.readline

def f(s, x, d, count):
    global ans
    if d>ans:
        return
    if 0 not in vis:
        ans=min(ans, d)
        return
    for i in range(n):
        if g[x][i]==0:
            continue
        if count!=n-1 and i==s:
            continue
        if not vis[i]:
            vis[i]=g[x][i]
            f(s, i, d+g[x][i], count+1)
            vis[i]=0

n=int(input())
g=[]
vis=[0]*n
ans=1e9
for i in range(n):
    g.append(list(map(int, input().split())))
for i in range(n):
    f(i, i, 0, 0)
print(ans)