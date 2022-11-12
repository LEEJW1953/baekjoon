import sys
input=sys.stdin.readline
from collections import deque

def BFS(arr, x, y, color):
    q=deque()
    q.append([x, y])
    arr[y][x]=0
    while q:
        [x, y] = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if arr[ny][nx]==color:
                arr[ny][nx]=0
                q.append([nx, ny])
    return

n=int(input())
arr1=[]
arr2=[]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
for i in range(n):
    arr3=[]
    arr4=[]
    color=input().strip()
    for j in color:
        arr3.append(j)
        if j=='R':
            arr4.append('G')
        else:arr4.append(j)
    arr1.append(arr3)
    arr2.append(arr4)
count1=0
count2=0
for i in range(n):
    for j in range(n):
        if arr1[i][j]!=0:
            count1+=1
            BFS(arr1, j, i, arr1[i][j])
        if arr2[i][j]!=0:
            count2+=1
            BFS(arr2, j, i, arr2[i][j])
print(count1, count2)