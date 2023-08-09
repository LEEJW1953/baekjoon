import sys
input=sys.stdin.readline

n=int(input())
INF=int(1e9)
side=[]
arr=[0]
dp=[INF]*300001
dp[0]=0
for i in range(1, 122):
    side.append(i*(i+1)//2)
for i in range(len(side)):
    arr.append(arr[i]+side[i])
for i in range(1, 300001):
    for j in range(1, len(arr)):
        t=arr[j]
        if i<t:
            break
        dp[i]=min(dp[i], dp[i-t]+1)
print(dp[n])