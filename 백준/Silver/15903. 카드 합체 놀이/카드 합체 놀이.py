import sys
input=sys.stdin.readline
import heapq

n, m = map(int, input().split())
arr=list(map(int, input().split()))
heapq.heapify(arr)
for i in range(m):
    a=heapq.heappop(arr)
    b=heapq.heappop(arr)
    heapq.heappush(arr, a+b)
    heapq.heappush(arr, a+b)
print(sum(arr))