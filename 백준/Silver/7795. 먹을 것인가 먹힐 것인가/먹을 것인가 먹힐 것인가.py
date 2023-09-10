import sys
input=sys.stdin.readline

def search(x, n):
    st=0
    en=n-1
    while st<=en:
        mid=(st+en)//2
        tmp=mid
        if b[mid]<x:
            st=mid+1
            tmp=st
        else:
            en=mid-1
            tmp=mid
    return tmp

t=int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    a.sort()
    b.sort()
    ans=0
    for i in a:
        ans+=search(i, m)
    print(ans)