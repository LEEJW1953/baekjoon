import sys
input=sys.stdin.readline
from heapq import heappop, heappush

n=int(input())
q=[]
for _ in range(n):
    x=int(input())
    if not x:
        if q:
            print(-heappop(q))
        else:
            print(0)
    else:
        heappush(q, -x)