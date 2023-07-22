import sys
input=sys.stdin.readline

def check(x):
    count=0
    for i in range(len(arr)):
        count+=arr[i]//x
    return count

def search():
    left=1
    right=max(arr)
    while left<=right:
        mid=(left+right)//2
        tmp=check(mid)
        if m<=tmp:
            left=mid+1
            tmp=mid
        else:
            right=mid-1
            tmp=right
    return tmp

n, k, m = map(int, input().split())
arr=[]
for _ in range(n):
    l=int(input())
    if l>=2*k:
        if l-2*k:
            arr.append(l-2*k)
    elif l>k:
        arr.append(l-k)
    else:
        continue
if arr and check(1)>=m:
    print(search())
else:
    print(-1)