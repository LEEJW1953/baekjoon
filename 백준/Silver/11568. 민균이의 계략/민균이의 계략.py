import sys
input=sys.stdin.readline
from bisect import bisect_left

n=int(input())
arr=list(map(int, input().split()))
dp=[arr[0]]
idx=[0]
for i in range(1, n):
    if arr[i]>dp[-1]:
        dp.append(arr[i])
        idx.append(i)
    else:
        target=bisect_left(dp, arr[i])
        dp[target]=arr[i]
        idx[target]=i
print(len(dp))