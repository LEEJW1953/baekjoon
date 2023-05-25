import sys
input=sys.stdin.readline

def search(x):
    s=0
    e=n-1
    while s<=e:
        mid=(s+e)//2
        tmp=(n-mid+1)*(mid+1)
        if tmp==x:
            return True
        if x<tmp:
            e=mid-1
        else:
            s=mid+1
    return False

n, k = map(int, input().split())
if search(k):
    print('YES')
else:
    print('NO')