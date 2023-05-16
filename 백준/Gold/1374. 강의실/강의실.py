import sys
input=sys.stdin.readline
import heapq

n=int(input())
heap=[]
ans=[]
for i in range(n):
    num, start, end = map(int, input().split())
    heapq.heappush(heap, [start, end, num])
start, end, num = heapq.heappop(heap)
heapq.heappush(ans, end)
while heap:
    start, end, num = heapq.heappop(heap)
    if ans[0]<=start:
        heapq.heappop(ans)
    heapq.heappush(ans, end)
print(len(ans))