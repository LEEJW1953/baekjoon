import sys
input=sys.stdin.readline

t=int(input())
dp=[0, 1, 2, 4, 7]
for i in range(4, 1000001):
    dp.append((dp[i-2]+dp[i-1]+dp[i])%1000000009)
for i in range(t):
    print(dp[int(input())])