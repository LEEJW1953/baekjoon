import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
ans=[0]*n
for i in range(n):
    t=arr[i]
    k=0
    for j in range(n):
        if ans[j]==0:
            k+=1
        if t<k:
            ans[j]=i+1
            break
print(*ans)