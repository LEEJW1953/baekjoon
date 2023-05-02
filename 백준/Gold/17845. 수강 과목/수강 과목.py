import sys
input=sys.stdin.readline

k, n = map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
dp=[[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if arr[i-1][1]<=j:
            dp[i][j]=max(dp[i-1][j], arr[i-1][0]+dp[i-1][j-arr[i-1][1]])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])