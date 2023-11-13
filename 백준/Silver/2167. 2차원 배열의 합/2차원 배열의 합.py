import sys
input=sys.stdin.readline

n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j]=sum(g[i-1][:j])+dp[i-1][j]
k=int(input())
for i in range(k):
    a,b,c,d=map(int, input().split())
    print(dp[c][d]-dp[c][b-1]-dp[a-1][d]+dp[a-1][b-1])