import sys
input=sys.stdin.readline

n=int(input())
coin=[1,2,5,7]
dp=[0]
for i in range(n):
    tmp=[]
    for j in range(4):
        if 0<=i+1-coin[j]:
            tmp.append(dp[i+1-coin[j]])
    dp.append(min(tmp)+1)
print(dp[n])