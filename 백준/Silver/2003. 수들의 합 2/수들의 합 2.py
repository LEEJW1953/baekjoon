import sys
input=sys.stdin.readline

n, m=map(int, input().split())
arr=list(map(int, input().split()))
s, e=0, 1
count=0
while e<=n:
    tmp=sum(arr[s:e])
    if tmp==m:
        count+=1
        s+=1
    if tmp<m:
        e+=1
    elif tmp>m:
        s+=1
print(count)