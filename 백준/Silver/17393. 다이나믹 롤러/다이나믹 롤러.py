import sys
input=sys.stdin.readline

def search(x):
    s=x
    e=n-1
    cur=arr1[x]
    res=i
    while s<=e:
        mid=(s+e)//2
        if arr2[mid]<=cur:
            s=mid+1
            res=mid
        else:
            e=mid-1
    return res

n=int(input())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
for i in range(n):
    tmp=search(i)
    print(tmp-i, end=' ')