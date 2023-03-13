import sys
input=sys.stdin.readline

def curve(arr, x, y):
    arr1=[]
    for i in range(len(arr)):
        arr1.append(arr[i])
    for i in range(len(arr)-2, -1, -1):
        arr1.append([x+arr[i][1]-y, y-arr[i][0]+x])
    return arr1

n=int(input())
dot=[[0]*105 for _ in range(105)]
dx=[0, -1, 0, 1]
dy=[1, 0, -1, 0]
count=0
for _ in range(n):
    y, x, d, g = map(int, input().split())
    arr=[]
    arr.append([x, y])
    arr.append([x+dx[d], y+dy[d]])
    for i in range(g):
        arr=curve(arr, arr[-1][0], arr[-1][1])
    for i in arr:
        if not dot[i[0]][i[1]]:
            dot[i[0]][i[1]]=1
for i in range(105):
    for j in range(105):
        if dot[i][j]==1 and dot[i+1][j]==1 and dot[i][j+1]==1 and dot[i+1][j+1]==1:
            count+=1
print(count)