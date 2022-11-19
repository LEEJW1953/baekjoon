import sys
input=sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int, input().split())
arr = [0] * f
arr[s-1]=1
dx = [u, -d]
q=deque([s-1])
tmp=False
while q:
    x = q.popleft()
    for i in range(2):
        nx = x + dx[i]
        if nx<0 or nx>=f:
            continue
        if arr[nx]==0:
            arr[nx] = arr[x]+1
            q.append(nx)
        if nx==(g-1):
            tmp=True
            break
    if tmp:
        break
if arr[g-1]!=0:
    print(arr[g-1]-1)
else:
    print('use the stairs')