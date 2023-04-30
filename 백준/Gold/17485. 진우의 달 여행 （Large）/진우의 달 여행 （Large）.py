import sys
input=sys.stdin.readline

n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
dp=[[[0]*3 for _ in range(m)] for _ in range(n)]
ans=1e9
for i in range(m):
    for j in range(3):
        dp[0][i][j]=g[0][i]
for i in range(1, n):
    for j in range(m):
        if j==0:
            dp[i][j][0]=1e9
            dp[i][j][1]=g[i][j]+min(dp[i-1][0][0], dp[i-1][0][2])
            dp[i][j][2]=g[i][j]+min(dp[i-1][1][0], dp[i-1][1][1])
        elif j==m-1:
            dp[i][j][0]=g[i][j]+min(dp[i-1][j-1][1], dp[i-1][j-1][2])
            dp[i][j][1]=g[i][j]+min(dp[i-1][j][0], dp[i-1][j][2])
            dp[i][j][2]=1e9
        else:
            dp[i][j][0]=g[i][j]+min(dp[i-1][j-1][1], dp[i-1][j-1][2])
            dp[i][j][1]=g[i][j]+min(dp[i-1][j][0], dp[i-1][j][2])
            dp[i][j][2]=g[i][j]+min(dp[i-1][j+1][0], dp[i-1][j+1][1])
for i in range(m):
    ans=min(ans, min(dp[-1][i]))
print(ans)