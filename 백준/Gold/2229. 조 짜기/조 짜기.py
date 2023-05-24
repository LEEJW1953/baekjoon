import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
dp=[0]*(n+1)
for i in range(n+1):
    for j in range(i):
        tmp=arr[i-j-1:i]
        dp[i]=max(dp[i], dp[i-j-1]+max(tmp)-min(tmp))
print(dp[-1])