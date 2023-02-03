import sys
input=sys.stdin.readline

n, k=map(int, input().split())
coin=[]
dp=[1e9]*10001
dp[0]=0
for _ in range(n):
    coin.append(int(input()))
coin.sort()
for i in range(k+1):
    for j in coin:
        if j<=i:
            dp[i]=min(dp[i-j]+1, dp[i])
if dp[k]!=1e9:
    print(dp[k])
else:
    print(-1)