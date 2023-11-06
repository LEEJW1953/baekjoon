import sys
input=sys.stdin.readline

n=int(input())
dp=[10000]*n
dp[0]=0
arr=list(map(int, input().split()))
for i in range(n):
    for j in range(1, arr[i]+1):
        tmp=i+j
        if tmp<n:
            dp[tmp]=min(dp[tmp], dp[i]+1)
print(dp[-1] if dp[-1]!=10000 else -1)