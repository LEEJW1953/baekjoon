import sys
input = sys.stdin.readline
from collections import deque

def hor(y, n):
    for i in range(9):
        if sdk[y][i]==n:
            return False
    return True

def ver(x, n):
    for i in range(9):
        if sdk[i][x]==n:
            return False
    return True

def sqr(x, y, n):
    nx = (x//3)*3
    ny = (y//3)*3
    for i in range(3):
        for j in range(3):
            if sdk[ny+i][nx+j]==n:
                return False
    return True

def DFS(n):
    if n==len(q):
        for i in range(9):
            print(*sdk[i])
        exit(0)
    [x, y] = q[n]
    for i in range(1,10):
        if ver(x, i) and hor(y, i) and sqr(x, y, i):
            sdk[y][x]=i
            DFS(n+1)
            sdk[y][x]=0

sdk=[]
q=[]
for i in range(9):
    arr=list(map(int, input().split()))
    sdk.append(arr)
    for j in range(9):
        if arr[j]==0:
            q.append([j, i])
DFS(0)