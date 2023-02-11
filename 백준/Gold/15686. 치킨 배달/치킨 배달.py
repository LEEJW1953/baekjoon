import sys
input=sys.stdin.readline
from collections import deque

def store(x):
    if len(arr)==m:
        dis(arr)
        return
    for i in range(x, len(chk)):
        arr.append(chk[i])
        store(i+1)
        arr.pop()

def dis(arr):
    global result
    count=0
    map=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j]==2 and [j, i] in arr:
                map[i][j]=2
            elif g[i][j]==1 or g[i][j]==0:
                map[i][j]=g[i][j]
    for i in range(n):
        for j in range(n):
            if map[i][j]==1:
                count+=distance(j, i, arr)
    result=min(result, count)
    return

def distance(x, y, arr):
    dist=1e11
    for i in range(len(arr)):
        dist=min(dist, (abs(arr[i][0]-x)+abs(arr[i][1]-y)))
    return dist

n, m = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
chk=[]
arr=[]
result=1e11
for i in range(n):
    for j in range(n):
        if g[i][j]==2:
            chk.append([j, i])
store(0)
print(result)