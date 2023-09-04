import sys
input=sys.stdin.readline

n=int(input())
g=[[0]*102 for _ in range(102)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
ans=0
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, a+10):
        for k in range(b, b+10):
            g[j][k]=1
for i in range(102):
    for j in range(102):
        for k in range(4):
            if g[i][j] and not g[i+dx[k]][j+dy[k]]:
                ans+=1
print(ans)