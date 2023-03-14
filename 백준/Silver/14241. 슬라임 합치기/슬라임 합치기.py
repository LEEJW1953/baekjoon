import sys
input=sys.stdin.readline
import heapq

n=int(input())
arr=list(map(int, input().split()))
heapq.heapify(arr)
score=0
while arr:
    tmp=heapq.heappop(arr)
    if not arr:
        break
    tmp1=heapq.heappop(arr)
    score+=tmp*tmp1
    heapq.heappush(arr, tmp+tmp1)
print(score)