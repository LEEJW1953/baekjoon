import sys
input=sys.stdin.readline

n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
k=int(input())
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    tmp=[0]
    for j in range(1, m+1):
        tmp.append(tmp[j-1]+g[i-1][j-1])
        dp[i][j]=dp[i-1][j]+tmp[j-1]+g[i-1][j-1]
for i in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])