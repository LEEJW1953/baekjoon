import sys
input=sys.stdin.readline

r, c, w = map(int, input().split())
g=[[1]*32 for _ in range(32)]
ans=0
for i in range(1, 32):
    for j in range(1, 32):
        g[i][j]=g[i-1][j]+g[i][j-1]
for i in range(w):
    ans+=sum(g[r-c+i][c-1:c+w-i-1])
print(ans)