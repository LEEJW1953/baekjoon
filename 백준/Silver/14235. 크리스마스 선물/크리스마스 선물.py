import sys
input=sys.stdin.readline
from heapq import heappush, heappop

n=int(input())
heap=[]
for i in range(n):
    arr=list(map(int, input().split()))
    if arr[0]==0:
        if heap:
            print(-1*heappop(heap))
        else:
            print(-1)
    else:
        for j in arr[1:]:
            heappush(heap, -1*j)