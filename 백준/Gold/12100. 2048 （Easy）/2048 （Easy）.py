import sys
input=sys.stdin.readline
from copy import deepcopy
from collections import deque

def game():
    if len(arr)==5:
        gg=deepcopy(g)
        move(arr, gg)
        return
    for i in range(4):
        arr.append(i)
        game()
        arr.pop()

def move(arr, gg):
    global answer
    ggg=deepcopy(gg)
    for i in range(5):
        result=[[0]*n for _ in range(n)]
        if arr[i]==0: # 위로 이동
            for j in range(n):
                q=deque()
                q1=deque()
                for k in range(n):
                    if ggg[k][j]:
                        q.append(ggg[k][j])
                while q:
                    tmp=q.popleft()
                    if q:
                        tmp1=q.popleft()
                        if tmp==tmp1:
                            q1.append(tmp*2)
                        else:
                            q1.append(tmp)
                            q.appendleft(tmp1)
                    else:
                        q1.append(tmp)
                for k in range(len(q1)):
                    result[k][j]=q1.popleft()
        elif arr[i]==1: # 왼쪽으로 이동
            for j in range(n):
                q=deque()
                q1=deque()
                for k in range(n):
                    if ggg[j][k]:
                        q.append(ggg[j][k])
                while q:
                    tmp=q.popleft()
                    if q:
                        tmp1=q.popleft()
                        if tmp==tmp1:
                            q1.append(tmp*2)
                        else:
                            q1.append(tmp)
                            q.appendleft(tmp1)
                    else:
                        q1.append(tmp)
                for k in range(len(q1)):
                    result[j][k]=q1.popleft()
        elif arr[i]==2: # 오른쪽으로 이동
            for j in range(n):
                q=deque()
                q1=deque()
                for k in range(n-1, -1, -1):
                    if ggg[j][k]:
                        q.append(ggg[j][k])
                while q:
                    tmp=q.popleft()
                    if q:
                        tmp1=q.popleft()
                        if tmp==tmp1:
                            q1.append(tmp*2)
                        else:
                            q1.append(tmp)
                            q.appendleft(tmp1)
                    else:
                        q1.append(tmp)
                for k in range(n-1, n-len(q1)-1, -1):
                    result[j][k]=q1.popleft()
        elif arr[i]==3: # 아래로 이동
            for j in range(n):
                q=deque()
                q1=deque()
                for k in range(n-1, -1, -1):
                    if ggg[k][j]:
                        q.append(ggg[k][j])
                while q:
                    tmp=q.popleft()
                    if q:
                        tmp1=q.popleft()
                        if tmp==tmp1:
                            q1.append(tmp*2)
                        else:
                            q1.append(tmp)
                            q.appendleft(tmp1)
                    else:
                        q1.append(tmp)
                for k in range(n-1, n-len(q1)-1, -1):
                    result[k][j]=q1.popleft()
        ggg=deepcopy(result)
    for i in range(n):
        for j in range(n):
            answer=max(answer, ggg[i][j])
    return

n=int(input())
g=[list(map(int, input().split())) for _ in range(n)]
answer=0
arr=[]
game()
print(answer)