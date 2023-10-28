import sys
input=sys.stdin.readline

n=int(input())
g=[list(map(int, input().split())) for _ in range(n)]
dx=[1, 0]
dy=[0, 1]
dp=[[0]*n for _ in range(n)]
dp[0][0]=1
for i in range(n):
    for j in range(n):
        if dp[i][j] and g[i][j]:
            x1, y1 = i+g[i][j], j
            x2, y2 = i, j+g[i][j]
            if 0<=x1<n and 0<=y1<n:
                dp[x1][y1]+=dp[i][j]
            if 0<=x2<n and 0<=y2<n:
                dp[x2][y2]+=dp[i][j]
print(dp[-1][-1])