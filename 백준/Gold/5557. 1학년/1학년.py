import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
dp=[[0]*21 for _ in range(n-1)]
dp[0][arr[0]]=1
for i in range(n-2):
    for j in range(21):
        k1, k2 = j+arr[i+1], j-arr[i+1]
        if dp[i][j] and 0<=k1<21:
            dp[i+1][k1]+=dp[i][j]
        if dp[i][j] and 0<=k2<21:
            dp[i+1][k2]+=dp[i][j]
print(dp[n-2][arr[n-1]])