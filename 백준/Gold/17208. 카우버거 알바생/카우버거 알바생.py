import sys
input=sys.stdin.readline

n, m, k = map(int, input().split())
order = [list(map(int, input().split())) for _ in range(n)]
dp=[[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        for l in range(1, k+1):
            c, f = order[i-1][0], order[i-1][1]
            if c<=j and f<=l:
                dp[i][j][l]=max(dp[i-1][j][l], 1+dp[i-1][j-c][l-f])
            else:
                dp[i][j][l]=dp[i-1][j][l]
print(dp[n][m][k])