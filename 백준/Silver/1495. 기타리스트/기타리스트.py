import sys
input=sys.stdin.readline

n, s, m = map(int, input().split())
v=list(map(int, input().split()))
dp=[[s]]
stop=False
result=-1
for i in range(n):
    arr=set()
    for j in range(len(dp[i])):
        tmp1=dp[i][j]+v[i]
        tmp2=dp[i][j]-v[i]
        if 0<=tmp1<=m:
            arr.add(tmp1)
        if 0<=tmp2<=m:
            arr.add(tmp2)
    arr=list(arr)
    if not arr:
        stop=True
        break
    else:
        dp.append(arr)
if not stop:
    result=max(dp[-1])
print(result)