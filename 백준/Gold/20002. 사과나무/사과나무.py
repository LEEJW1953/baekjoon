import sys
input=sys.stdin.readline

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
new=[[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        new[i][j]=new[i-1][j]+new[i][j-1]-new[i-1][j-1]+arr[i-1][j-1]
ans=-1e9
for i in range(1, n+1):
    for j in range(n+1-i):
        for k in range(n+1-i):
            ans=max((new[j+i][k+i]-new[j][k+i]-new[j+i][k]+new[j][k]), ans)
print(ans)