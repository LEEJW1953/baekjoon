import sys
input=sys.stdin.readline

n, m = map(int,input().split())
aa=[]
bb=[]
for i in range(n):
    aa.append(list(map(int, input().split())))
m, k = map(int,input().split())
for i in range(m):
    bb.append(list(map(int, input().split())))
answer=[[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            answer[i][j]+=aa[i][l]*bb[l][j]
for i in range(n):
    for j in range(k):
        if j==k-1:
            print(answer[i][j])
        else:
            print(answer[i][j], end=' ')