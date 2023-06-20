import sys
input=sys.stdin.readline
from collections import defaultdict

n=int(input())
arr=[]
d=defaultdict(int)
for i in range(n):
    s=input().strip()
    arr.append(s)
    d[s]+=1
for i in range(n-1):
    s=input().strip()
    d[s]-=1
for i in range(n):
    if d[arr[i]]:
        print(arr[i])
        exit(0)