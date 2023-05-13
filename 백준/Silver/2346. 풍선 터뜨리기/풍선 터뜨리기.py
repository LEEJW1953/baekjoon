import sys
input=sys.stdin.readline
from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))
arr=[]
while q:
    index, num=q.popleft()
    arr.append(index+1)
    if num>0:
        q.rotate(-(num-1))
    else:
        q.rotate(-num)
print(' '.join(map(str, arr)))