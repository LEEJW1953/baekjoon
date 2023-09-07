import sys
input=sys.stdin.readline

n=int(input())
arr=[int(input()) for _ in range(n)]
arr.sort(reverse=True)
ans=0
for i in range(n):
    tmp=arr[i]-i
    if tmp>0:
        ans+=tmp
print(ans)