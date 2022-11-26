import sys
input=sys.stdin.readline
import heapq

n, m = map(int, input().split())
arr=list(map(int, input().split()))
heapq.heapify(arr)
for i in range(m):
    a=heapq.heappop(arr)
    b=heapq.heappop(arr)
    arr.append(a+b)
    arr.append(a+b)
    heapq.heapify(arr)
print(sum(arr))