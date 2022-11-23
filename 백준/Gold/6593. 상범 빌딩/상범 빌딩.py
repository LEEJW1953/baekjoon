import sys
input=sys.stdin.readline
from collections import deque

def BFS(k, j, i):
    q=deque()
    q.append([k, j, i])
    while q:
        [x, y, z] = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= c or ny < 0 or ny >= r or nz < 0 or nz >= l:
                continue
            if arr[nz][ny][nx] != "#":
                if arr[nz][ny][nx] == ".":
                    arr[nz][ny][nx] = arr[z][y][x] + 1
                    q.append([nx, ny, nz])
                elif arr[nz][ny][nx] == "E":
                    arr[nz][ny][nx] = arr[z][y][x] + 1
                    print(f"Escaped in {arr[nz][ny][nx]} minute(s).")
                    return
    print("Trapped!")
    return

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while True:
    l, r, c = map(int, input().split())
    if l==0:
        break
    arr=[]
    for i in range(l):
        arr1=[]
        for j in range(r):
            arr2=[]
            for k in input().strip():
                arr2.append(k)
            arr1.append(arr2)
        arr.append(arr1)
        input()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr[i][j][k]=="S":
                    arr[i][j][k]=0
                    BFS(k, j, i)