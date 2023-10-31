import sys
input=sys.stdin.readline
from heapq import heappush, heappop

n=int(input())
q=[]
for i in range(n):
    x=int(input())
    if x==0:
        if q:
            target=heappop(q)
            print(target[1])
        else:
            print(0)
    else:
        heappush(q, [abs(x), x])