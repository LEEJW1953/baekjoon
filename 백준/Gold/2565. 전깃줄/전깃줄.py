import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    x, y=map(int, input().split())
    arr.append([x,y])
arr.sort(key=lambda x : x[0])
dp=[1]*n
for i in range(n):
    for j in range(i):
        if arr[j][1]<arr[i][1]:
            dp[i]=max(dp[i], dp[j]+1)
print(n-max(dp))