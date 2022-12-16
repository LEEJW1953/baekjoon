import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
m=int(input())
dp=[0]
for i in range(n):
    dp.append(dp[i]+arr[i])
for i in range(m):
    a, b=map(int, input().split())
    print(dp[b]-dp[a-1])