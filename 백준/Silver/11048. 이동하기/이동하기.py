import sys
input=sys.stdin.readline

n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
move=[[0, 1], [1, 0], [1, 1]]
dp=[[0]*m for _ in range(n)]
dp[0][0]=g[0][0]
for i in range(n):
    for j in range(m):
        for k in range(3):
            nx, ny = i+move[k][0], j+move[k][1]
            if 0<=nx<n and 0<=ny<m:
                dp[nx][ny]=max(dp[i][j]+g[nx][ny],dp[nx][ny])
print(dp[-1][-1])