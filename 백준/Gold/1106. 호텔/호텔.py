import sys
input=sys.stdin.readline

c,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [1e7 for _ in range(c+100)]
dp[0]=0
for cost, guest in arr:
    for i in range(guest,c+100):
        dp[i] = min(dp[i-guest]+cost,dp[i])
print(min(dp[c:]))