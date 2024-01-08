import sys
input=sys.stdin.readline
from itertools import combinations_with_replacement as com

n=int(input())
arr=[1,5,10,50]
res=set()
for i in com(arr, n):
    res.add(sum(i))
print(len(res))