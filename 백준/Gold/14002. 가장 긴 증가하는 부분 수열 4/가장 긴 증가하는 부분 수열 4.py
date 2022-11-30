import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
dp=[1]*n
for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i], dp[j]+1)
print(max(dp))
arr1=[0]
tmp=max(dp)
for i in range(n-1, -1, -1):
    if dp[i]==tmp:
        arr1.append(arr[i])
        tmp-=1
for i in range(len(arr1)-1, 0, -1):
    print(arr1[i], end=' ')