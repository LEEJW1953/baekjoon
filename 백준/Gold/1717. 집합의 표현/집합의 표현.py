import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if arr[x]!=x:
        arr[x]=find(arr[x])
    return arr[x]

def union(x, y):
    x=find(x)
    y=find(y)
    if x<y:
        arr[y]=x
    else:
        arr[x]=y

n, m = map(int, input().split())
arr=list(range(n+1))
for i in range(m):
    a, b, c = map(int, input().split())
    if a==0:
        union(b, c)
    else:
        if find(b)==find(c):
            print('YES')
        else:
            print('NO')