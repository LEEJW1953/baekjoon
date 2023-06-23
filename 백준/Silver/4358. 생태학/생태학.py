import sys
input=sys.stdin.readline
from collections import defaultdict

d=defaultdict(int)
total=0
while True:
    s=input().strip()
    if not s:
        break
    total+=1
    d[s]+=1
arr=list(d.items())
arr.sort()
for i in range(len(arr)):
    print(arr[i][0], '{:.4f}'.format(arr[i][1]/total*100))