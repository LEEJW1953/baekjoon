import sys
input=sys.stdin.readline

n, m = map(int, input().split())
k=int(input())
res=[[0]*(m+1) for _ in range(n+1)]
res[0][0]=1
arr=[]
for _ in range(k):
    a, b, c, d = map(int, input().split())
    arr.append([min(a, c), min(b, d), max(a, c), max(b, d)])
for i in range(1, n+1):
    x, nx = i-1, i
    tmp=True
    for l in range(k):
        a=arr[l][0]
        b=arr[l][1]
        c=arr[l][2]
        d=arr[l][3]
        if (x, 0, nx, 0)==(a, b, c, d):
            tmp=False
    if tmp:
        res[i][0]+=res[i-1][0]

for i in range(1, m+1):
    y, ny = i-1, i
    tmp=True
    for l in range(k):
        a=arr[l][0]
        b=arr[l][1]
        c=arr[l][2]
        d=arr[l][3]
        if (0, y, 0, ny)==(a, b, c, d):
            tmp=False
    if tmp:
        res[0][i]+=res[0][i-1]

for i in range(1, n+1):
    for j in range(1, m+1):
        x1, y1, x2, y2, nx, ny = i-1, j, i, j-1, i, j
        tmp1, tmp2 = True, True
        for l in range(k):
            a=arr[l][0]
            b=arr[l][1]
            c=arr[l][2]
            d=arr[l][3]
            if (x1, y1, nx, ny)==(a, b, c, d):
                tmp1=False
            if (x2, y2, nx, ny)==(a, b, c, d):
                tmp2=False
        if tmp1:
            res[nx][ny]+=res[x1][y1]
        if tmp2:
            res[nx][ny]+=res[x2][y2]
print(res[-1][-1])