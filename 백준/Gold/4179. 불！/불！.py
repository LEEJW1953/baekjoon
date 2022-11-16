import sys
input=sys.stdin.readline
from collections import deque

def BFS():
    global result
    while True:
        result+=1
        temp=[]
        while floc:
            [x, y] = floc.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or nx>=c or ny<0 or ny>=r:
                    continue
                if arr[ny][nx]=='.' or arr[ny][nx]==1:
                    arr[ny][nx]='F'
                    temp.append([nx, ny])
        if temp:
            for i in range(len(temp)):
                floc.append(temp[i])
        temp=[]
        while jloc:
            [x, y] = jloc.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or nx>=c or ny<0 or ny>=r:
                    return result
                if arr[ny][nx]=='.':
                    arr[y][x]=1
                    arr[ny][nx]='J'
                    temp.append([nx, ny])
        if temp:
            for i in range(len(temp)):
                jloc.append(temp[i])
        if not jloc:
            return False
r, c=map(int, input().split())
arr=[]
jloc=deque()
floc=deque()
result=0
for i in range(r):
    arr1=list(input().strip())
    for j in range(c):
        if arr1[j]=='J':
            jloc.append([j, i])
        elif arr1[j]=='F':
            floc.append([j, i])
    arr.append(arr1)
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
if BFS():
    print(result)
else:
    print('IMPOSSIBLE')