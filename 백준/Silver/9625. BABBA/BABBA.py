import sys
input=sys.stdin.readline

k=int(input())
dp=[[0, 1]]
for i in range(k):
    arr=[]
    arr.append(dp[i][1])
    arr.append(dp[i][0]+dp[i][1])
    dp.append(arr)
print(dp[k-1][0], dp[k-1][1])