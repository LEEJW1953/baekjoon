import sys
input=sys.stdin.readline
from collections import defaultdict

k, l = map(int, input().split())
dic={}
for i in range(l):
    dic[str(input().strip())]=i
arr=sorted(dic.items(), key=lambda x:x[1])
if len(arr)<k:
    for i in range(len(arr)):
        print(arr[i][0])
else:
    for i in range(k):
        print(arr[i][0])