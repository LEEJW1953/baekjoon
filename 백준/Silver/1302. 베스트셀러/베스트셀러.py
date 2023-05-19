import sys
input=sys.stdin.readline
from collections import defaultdict

n=int(input())
d=defaultdict(int)
for i in range(n):
    d[input().strip()]+=1
arr=list(d.items())
arr.sort(key=lambda x:(-x[1], x[0]))
print(arr[0][0])