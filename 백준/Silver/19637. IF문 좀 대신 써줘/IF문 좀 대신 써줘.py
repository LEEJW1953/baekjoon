import sys
input=sys.stdin.readline

def search(target):
    s, e=0, n-1
    while s<=e:
        mid=(s+e)//2
        if target<=int(stat[mid][1]):
            e=mid-1
        else:
            s=mid+1
    return e+1

n, m=map(int, input().split())
stat=[list(map(str, input().split())) for _ in range(n)]
for _ in range(m):
    c=int(input())
    print(stat[search(c)][0])