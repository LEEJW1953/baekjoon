import sys

def com(x):
    return (x*(x-1))//2

n, m = map(int, input().split())
arr=list(map(int, sys.stdin.readline().split()))
for i in range(n):
    arr[i]%=m
dp=[0]
for i in range(n):
    dp.append((dp[i]+arr[i])%m)
arr1=[0]*m
for i in range(len(dp)):
    arr1[dp[i]]+=1
result=0
for i in range(m):
    result+=com(arr1[i])
print(result)