import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
dp=[[0]*n for _ in range(n)]
ans=[0]*(n)
for i in range(n):
    minn, maxx = arr[i], arr[i]
    for j in range(i, n):
        minn=min(minn, arr[j])
        maxx=max(maxx, arr[j])
        dp[i][j]=maxx-minn
for i in range(n):
    for j in range(i):
        ans[i]=max(ans[i], ans[j-1]+dp[j][i])
print(ans[-1])