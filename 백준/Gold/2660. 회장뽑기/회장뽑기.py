import sys
input=sys.stdin.readline

n=int(input())
g=[[100]*n for _ in range(n)]
ans=[100]
for i in range(n):
    g[i][i]=0
while True:
    a, b = map(int, input().split())
    if a==-1 and b==-1:
        break
    g[a-1][b-1]=1
    g[b-1][a-1]=1
for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j]=min(g[i][j], g[i][k]+g[k][j])
for i in range(n):
    del g[i][i]
for i in range(n):
    ans[0]=min(ans[0], max(g[i]))
for i in range(n):
    if max(g[i])==ans[0]:
        ans.append(i+1)
print(ans[0], len(ans)-1)
print(*ans[1:])