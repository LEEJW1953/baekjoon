import sys
input=sys.stdin.readline
from collections import defaultdict

arr=[]
d=defaultdict(int)
total=0
while True:
    s=input().strip()
    if not s:
        break
    if s not in arr:
        arr.append(s)
    total+=1
    d[s]+=1
arr.sort()
for i in range(len(arr)):
    print(arr[i], '{:.4f}'.format(d[arr[i]]/total*100))