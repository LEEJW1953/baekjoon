import sys
from collections import deque
input=sys.stdin.readline

def dfs(n):
    visited[n]=True
    print(n, end=' ')
    for i in arr[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    queue=deque([n])
    visited[n]=True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in arr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

n, m, v=map(int, input().split())
arr=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    a, b=map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(n+1):
    arr[i].sort()
dfs(v)
print()
visited=[False]*(n+1)
bfs(v)