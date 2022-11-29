import sys
input=sys.stdin.readline

t, w = map(int, input().split())
arr=[]
dp=[[0]*(t+1) for _ in range(w+1)]
result=[]
for i in range(t):
    arr.append(int(input()))
for i in range(t):
    if arr[i]==1:
        dp[0][i+1]=dp[0][i]+1
    else:
        dp[0][i+1]=dp[0][i]
result.append(dp[0][-1])
for i in range(1, w+1):
    for j in range(1, t+1):
        if i%2==1:
            if arr[j-1]==2:
                dp[i][j]=max(dp[i][j-1]+1, dp[i-1][j-1])
            else:
                dp[i][j]=max(dp[i-1][j-1]+1, dp[i][j-1])
        else:
            if arr[j-1]==1:
                dp[i][j]=max(dp[i][j-1]+1, dp[i-1][j-1])
            else:
                dp[i][j]=max(dp[i-1][j-1]+1, dp[i][j-1])
    result.append(dp[i][-1])
print(max(result))