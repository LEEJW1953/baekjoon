import sys
input=sys.stdin.readline
from heapq import heappush, heappop

n=int(input())
h=[]
for i in range(n):
    x=int(input())
    if not x:
        if h:
            print(heappop(h))
        else:
            print(0)
    else:
        heappush(h, x)