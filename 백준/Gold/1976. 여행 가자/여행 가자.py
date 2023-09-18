import sys
input=sys.stdin.readline

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a, b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
    return

n=int(input())
m=int(input())
g=[]
parent=list(range(n))
for i in range(n):
    g.append(list(map(int, input().split())))
arr=list(map(int, input().split()))
for i in range(n):
    for j in range(i, n):
        if g[i][j]:
            union(i, j)
for i in range(len(arr)-1):
    if find(arr[i]-1)!=find(arr[i+1]-1):
        print('NO')
        exit(0)
print('YES')