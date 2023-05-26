import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(100000)

def dfs(start, parent, total):
    global ans, node
    if total>ans:
        ans=total
        node=start
    q=deque()
    for i in range(len(g[start])):
        if parent!=g[start][i][0]:
            q.append(g[start][i])
    while q:
        [x, y]=q.pop()
        dfs(x, start, total+y)

n=int(input())
g=[[]for _ in range(n)]
ans=0
node=-1
for i in range(n-1):
    a, b, c = map(int, input().split())
    g[a-1].append([b-1, c])
    g[b-1].append([a-1, c])
dfs(0, 0, 0)
dfs(node, node, 0)
print(ans)