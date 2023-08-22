import sys
input=sys.stdin.readline
from collections import defaultdict

n=int(input())
arr=[]
for i in range(n):
    s=input().strip()
    arr.append(s)
for i in range(1, len(arr[0])+1):
    d=defaultdict(int)
    tmp=True
    for j in arr:
        d[j[-i:]]+=1
        if d[j[-i:]]>1:
            tmp=False
            break
    if tmp:
        print(i)
        break