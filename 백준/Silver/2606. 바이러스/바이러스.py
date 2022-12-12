import sys
input=sys.stdin.readline
from collections import deque

def dfs():
    q=deque()
    q.append(0)
    while q:
        x=q.pop()
        for i in range(c):
            if g[x][i]==1 and i not in vis:
                vis.append(i)
                q.append(i)
    return

c=int(input())
n=int(input())
arr=[]
g=[[0]*c for _ in range(c)]
vis=[0]
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in arr:
    g[i[0]-1][i[1]-1]=1
    g[i[1]-1][i[0]-1]=1
dfs()
print(len(vis)-1)