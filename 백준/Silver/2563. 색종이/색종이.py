import sys
input=sys.stdin.readline

n=int(input())
arr=[[0]*100 for _ in range(100)]
ans=0
for i in range(n):
    x, y = map(int,input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            arr[j][k]=1
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            ans+=1
print(ans)