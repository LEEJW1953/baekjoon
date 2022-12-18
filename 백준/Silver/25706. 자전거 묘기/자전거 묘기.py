import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
dp=[1]
if n>1:
    for i in range(n-2, -1, -1):
        if arr[i]+i+1>=n:
            dp.append(1)
        else:
            dp.append(dp[n-(arr[i]+i+2)]+1)
for i in range(len(dp)):
    print(dp[len(dp)-1-i], end=' ')