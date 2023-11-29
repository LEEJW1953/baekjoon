import sys
input=sys.stdin.readline

def check(x):
    count=1
    tmp=0
    for i in range(n):
        if arr[i]>x:
            return False
        if tmp<=x-arr[i]:
            tmp+=arr[i]
        else:
            count+=1
            tmp=arr[i]
    return count<=m

n, m = map(int, input().split())
arr=list(map(int, input().split()))
st, en = 0, sum(arr)
while st<=en:
    mid=(st+en)//2
    tmp=check(mid)
    if tmp:
        ans=mid
        en=mid-1
    else:
        st=mid+1
        ans=st
print(ans)