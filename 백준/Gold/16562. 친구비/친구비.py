import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

def find(x):
    if x!=arr[x]:
        arr[x]=find(arr[x])
    return arr[x]

def union(x, y):
    x=find(x)
    y=find(y)
    if x!=y:
        if price[x-1]<price[y-1]:
            arr[y]=x
        else:
            arr[x]=y

n, m, k = map(int, input().split())
price = list(map(int, input().split()))
arr=list(range(n+1))
total=0
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
for i in range(1, n+1):
    if i==arr[i]:
        total+=price[i-1]
if total<=k:
    print(total)
else:
    print('Oh no')