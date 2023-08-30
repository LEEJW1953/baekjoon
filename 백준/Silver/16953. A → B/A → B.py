import sys
input=sys.stdin.readline
from collections import deque

def bfs(a, b):
    q=deque()
    q.append([a, 1])
    d={}
    d[a]=1
    while q:
        [cur, cnt]=q.popleft()
        if cur==b:
            return cnt
        new1=cur*2
        new2=cur*10+1
        if new1<=b and new1 not in d:
            q.append([new1, cnt+1])
            d[new1]=1
        if new2<=b and new2 not in d:
            q.append([new2, cnt+1])
            d[new2]=1
    return -1

a, b = map(int, input().split())
print(bfs(a, b))