import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
arr=[0]
arr1=[]
for i in range(m):
    arr.append(int(input()))
    arr1.append(arr[i+1]-1-arr[i])
arr1.append(n-arr[-1])
dp=[1, 1, 2, 3]
for i in range(3, 40):
    dp.append(dp[i-1]+dp[i])
result=1
for i in range(len(arr1)):
    result*=dp[arr1[i]]
print(result)