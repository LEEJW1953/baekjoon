import sys
input=sys.stdin.readline

def search(target, index):
    s, e=index, n-1
    tmp=-1
    while s<=e:
        mid=(s+e)//2
        if file[mid]*0.9<=target:
            tmp=mid
            s=mid+1
        else:
            e=mid-1
    if tmp!=-1:
        return tmp
    return index

n=int(input())
file=list(map(int, input().split()))
file.sort()
ans=0
for i in range(n):
    ans+=search(file[i], i)-i
print(ans)