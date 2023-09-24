import sys
input=sys.stdin.readline

def count(arr):
    res=1
    c=1
    tmp = arr[0]
    for i in range(1, len(arr)):
        if tmp==arr[i]:
            c+=1
        else:
            tmp=arr[i]
            c=1
        res=max(res, c)
    return res

def f(case, x, y, nx, ny):
    t1=g[x][y]
    t2=g[nx][ny]
    res=1
    if case==0:
        s1, c1 = g[x][:], 1
        s2, c2 = g[nx][:], 1
        s3, c3 = [], 1
        for i in range(n):
            s3.append(g[i][y])
        s1[y]=t2
        s2[y]=t1
        s3[x]=t2
        s3[nx]=t1
    if case==1:
        s1, c1 = g[x][:], 1
        s2, c2 = [], 1
        s3, c3 = [], 1
        for i in range(n):
            s2.append(g[i][y])
            s3.append(g[i][ny])
        s1[y]=t2
        s1[ny]=t1
        s2[x]=t2
        s3[x]=t1
    tmp1, tmp2, tmp3 = s1[0], s2[0], s3[0]
    for i in range(1, n):
        if tmp1==s1[i]:
            c1+=1
        else:
            tmp1=s1[i]
            c1=1
        if tmp2==s2[i]:
            c2+=1
        else:
            tmp2=s2[i]
            c2=1
        if tmp3==s3[i]:
            c3+=1
        else:
            tmp3=s3[i]
            c3=1
        res=max(res, c1, c2, c3)
    return res

n=int(input())
g=[list(input().strip()) for _ in range(n)]
dx=[1, 0]
dy=[0, 1]
ans=0
for x in range(n):
    ans=max(ans, count(g[x]))
    arr=[]
    for y in range(n):
        arr.append(g[x][y])
        for k in range(2):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if g[x][y]!=g[nx][ny]:
                    ans=max(ans, f(k, x, y, nx, ny))
    ans=max(ans, count(arr))
print(ans)