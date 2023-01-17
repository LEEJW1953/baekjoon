import sys
input=sys.stdin.readline

n, m=map(int, input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr=list(set(arr))
arr.sort()
s=0
e=0
ans=1e11
while s<len(arr):
    tmp=arr[e]-arr[s]
    if tmp==m:
        ans=m
        break
    elif tmp>m:
        ans=min(ans, tmp)
        s+=1
    else:
        e+=1
    if e>=len(arr):
        break
print(ans)