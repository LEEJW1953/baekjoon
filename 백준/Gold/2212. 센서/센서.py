import sys
input=sys.stdin.readline

n=int(input())
k=int(input())
arr=list(set(map(int, input().split())))
arr.sort()
dp=[]
for i in range(len(arr)-1):
    dp.append(arr[i+1]-arr[i])
dp.sort()
print(sum(dp[:(len(dp)-(k-1))]))