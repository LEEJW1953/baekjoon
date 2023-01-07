import sys
input=sys.stdin.readline

n=int(input())
num=list(map(int, input().split()))
dp=[[0]*n for _ in range(n)]
m=int(input())
for i in range(n):
    for j in range(n):
        if i==j:
            dp[i][j]=1
        elif j==i+1:
            if num[j]==num[i]:
                dp[i][j]=1
for i in range(2, n):
    for j in range(n-i):
        if num[j]==num[j+i] and dp[j+1][j+i-1]:
            dp[j][j+i]=1
for i in range(m):
    s, e=map(int, input().split())
    print(dp[s-1][e-1])