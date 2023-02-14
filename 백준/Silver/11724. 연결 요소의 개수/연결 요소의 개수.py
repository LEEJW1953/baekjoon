import sys
input=sys.stdin.readline
from collections import deque

def bfs(x, count):
    q=deque()
    q.append(x)
    if not arr[x]:
        arr[x]=count
    while q:
        target=q.popleft()
        for i in range(len(g[target])):
            if not arr[g[target][i]]:
                arr[g[target][i]]=count
                q.append(g[target][i])
    return

n, m = map(int, input().split())
g=[[]*(n+1) for _ in range(n+1)]
arr=[0]*(n+1)
count=1
answer=0
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(1, n+1):
    bfs(i, count)
    count=arr[i]+1
for i in range(len(arr)):
    answer=max(answer, arr[i])
print(answer)