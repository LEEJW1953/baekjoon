import sys
input=sys.stdin.readline

def find(x):
    if x!=g[x]:
        g[x]=find(g[x])
    return g[x]

def union(x, y):
    x=find(x)
    y=find(y)
    if x<y:
        g[y]=x
    else:
        g[x]=y

n, m = map(int, input().split())
g=list(range(n))
ans=0
for i in range(m):
    a, b = map(int, input().split())
    if find(a)==find(b) and not ans:
        ans=i+1
    else:
        union(a, b)
print(ans)