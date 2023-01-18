import sys
input=sys.stdin.readline

n, s=map(int, input().split())
arr=list(map(int, input().split()))
ans=0
dp=[0]
for i in range(n):
    dp.append(dp[i]+arr[i])
start, end=0, 1
while start<=n and end<=n:
    tmp=dp[end]-dp[start]
    if tmp>=s:
        if ans==0:
            ans=end-start
        else:
            ans=min(ans, end-start)
        start+=1
    else:
        end+=1
print(ans)