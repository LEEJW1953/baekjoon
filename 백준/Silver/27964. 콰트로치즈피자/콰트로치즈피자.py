import sys
input=sys.stdin.readline
from collections import defaultdict

n=int(input())
arr=list(map(str, input().split()))
d=defaultdict(int)
for i in arr:
    if len(i)<6:
        continue
    if i[-6:]=='Cheese':
        d[i]+=1
ans=len(d.keys())
if ans>=4:
    print('yummy')
else:
    print('sad')