import sys
input=sys.stdin.readline

n, k=map(int, input().split())
arr=[]
dp=[0]*(k+1)
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(len(arr)):
    w,v=arr[i][0],arr[i][1]
    for j in range(k, w-1, -1):
        dp[j]=max(dp[j], dp[j-w]+v)
print(max(dp))