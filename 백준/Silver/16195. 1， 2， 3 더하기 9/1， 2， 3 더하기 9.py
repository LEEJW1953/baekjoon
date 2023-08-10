import sys
input=sys.stdin.readline
from collections import defaultdict

t=int(input())
dp=[{}, {1:1}, {1:1, 2:1}, {1:1, 2:2, 3:1}, {1:0, 2:3, 3:3, 4:1}]
for i in range(5, 1001):
    d=defaultdict(int)
    d[1]=0
    for j in range(1, i):
        a, b, c = 0, 0, 0
        if j in dp[i-1]:
            a=dp[i-1][j]
        if j in dp[i-2]:
            b=dp[i-2][j]
        if j in dp[i-3]:
            c=dp[i-3][j]
        d[j+1]=(a+b+c)%1000000009
    dp.append(d)
for i in range(t):
    n, m = map(int, input().split())
    count=0
    for j in range(m+1):
        if j in dp[n]:
            count+=dp[n][j]%1000000009
    print(count%1000000009)