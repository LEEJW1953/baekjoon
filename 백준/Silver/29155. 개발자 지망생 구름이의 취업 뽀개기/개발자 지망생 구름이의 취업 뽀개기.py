import sys
input=sys.stdin.readline

n=int(input())
p=list(map(int, input().split()))
arr=[[] for _ in range(5)]
ans=240
for i in range(n):
    k, t = map(int, input().split())
    arr[k-1].append(t)
for i in range(5):
    arr[i].sort()
    tmp=arr[i][0]
    ans+=tmp
    for j in range(p[i]-1):
        ans+=arr[i][j+1]*2-tmp
        tmp=arr[i][j+1]
print(ans)