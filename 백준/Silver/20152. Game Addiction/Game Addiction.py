import sys
input=sys.stdin.readline

h, n = map(int, input().split())
x=abs(h-n)+1
dp=[[0]*x for _ in range(x)]
for i in range(x):
    dp[i][0]=1
for i in range(1, x):
    for j in range(1, x):
        if i>=j:
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[-1][-1])