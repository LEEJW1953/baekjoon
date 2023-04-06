import sys
input=sys.stdin.readline
from collections import deque

n = int(input())
arr=list(map(int, input().split()))
vis={}
ans=0
dbl=0
q=deque()
q.append(1)
vis[1]=[1, 0]
while q:
    i=q.popleft()
    if i*2 not in vis.keys() and i*2<=1000:
        vis[i*2]=[vis[i][0], vis[i][1]+1]
        q.append(i*2)
    if i+1 not in vis.keys() and i+1<=1000:
        vis[i+1]=[vis[i][0]+1, vis[i][1]]
        q.append(i+1)
for i in range(n):
    if arr[i]==0:
        continue
    ans+=vis[arr[i]][0]
    dbl=max(dbl, vis[arr[i]][1])
ans+=dbl
print(ans)