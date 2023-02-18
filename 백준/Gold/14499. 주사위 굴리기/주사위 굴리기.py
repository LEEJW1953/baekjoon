import sys
input=sys.stdin.readline
from copy import deepcopy

def move(nn):
    global x, y, dice
    if nn==1 and y<m-1:
        y+=1
        new=[2, 1, 5, 0, 4, 3]
        newdice=[]
        for i in new:
            newdice.append(dice[i])
        dice=deepcopy(newdice)
        if not g[x][y]:
            g[x][y]=dice[0]
        else:
            dice[0]=g[x][y]
            g[x][y]=0
        print(dice[5])
        return
    elif nn==2 and 0<y:
        y-=1
        new=[3, 1, 0, 5, 4, 2]
        newdice=[]
        for i in new:
            newdice.append(dice[i])
        dice=deepcopy(newdice)
        if not g[x][y]:
            g[x][y]=dice[0]
        else:
            dice[0]=g[x][y]
            g[x][y]=0
        print(dice[5])
        return
    elif nn==3 and 0<x:
        x-=1
        new=[1, 5, 2, 3, 0, 4]
        newdice=[]
        for i in new:
            newdice.append(dice[i])
        dice=deepcopy(newdice)
        if not g[x][y]:
            g[x][y]=dice[0]
        else:
            dice[0]=g[x][y]
            g[x][y]=0
        print(dice[5])
        return
    elif nn==4 and x<n-1:
        x+=1
        new=[4, 0, 2, 3, 5, 1]
        newdice=[]
        for i in new:
            newdice.append(dice[i])
        dice=deepcopy(newdice)
        if not g[x][y]:
            g[x][y]=dice[0]
        else:
            dice[0]=g[x][y]
            g[x][y]=0
        print(dice[5])
        return
    return

n, m, x, y, k = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
arr=list(map(int, input().split()))
dice=[0]*6
for i in range(k):
    move(arr[i])