import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    q=deque()
    q.append((1, 0))
    while q:
        (show, clip) = q.popleft()
        if show==s:
            print(vis[(show, clip)])
            break
        if (show, show) not in vis.keys():
            vis[(show, show)]=vis[(show, clip)]+1
            q.append((show, show))
        if (show+clip, clip) not in vis.keys():
            vis[(show+clip, clip)]=vis[(show, clip)]+1
            q.append((show+clip, clip))
        if (show-1, clip) not in vis.keys():
            vis[(show-1, clip)]=vis[(show, clip)]+1
            q.append((show-1, clip))

s=int(input())
vis=dict()
vis[(1, 0)]=0
bfs()