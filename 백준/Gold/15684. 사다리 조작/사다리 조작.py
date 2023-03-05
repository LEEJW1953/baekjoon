import sys
input=sys.stdin.readline

def ladder(count, limit):
    global answer
    for i in range(n):
        tmp=i
        for j in range(h):
            if tmp==0:
                if arr[j][0]:
                    tmp=1
            elif 0<tmp<n-1:
                if arr[j][tmp-1]:
                    tmp-=1
                elif arr[j][tmp]:
                    tmp+=1
            else:
                if arr[j][tmp-1]:
                    tmp-=1
        if tmp!=i:
            return
    answer=min(answer, count)
    if answer==limit:
        print(limit)
        exit(0)
    return

def newladder(x, y, depth, limit):
    if depth==limit:
        ladder(depth, limit)
        return
    for i in range(x, h):
        for j in range(n-1):
            if i==x and j<=y:
                continue
            if arr[i][j]==0:
                if j==0 and arr[i][j]==0:
                    arr[i][j]=1
                    newladder(i, j, depth+1, limit)
                    arr[i][j]=0
                elif j==n-2 and arr[i][j-1]==0:
                    arr[i][j]=1
                    newladder(i, j, depth+1, limit)
                    arr[i][j]=0
                elif 0<j<n-2 and arr[i][j]==0 and arr[i][j-1]==0:
                    arr[i][j]=1
                    newladder(i, j, depth+1, limit)
                    arr[i][j]=0
    return

n, m, h = map(int, input().split())
arr=[[0]*(n-1) for _ in range(h)]
answer=1e9
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1]=1
ladder(0, 0)
for k in range(1, 4):
    for i in range(h):
        for j in range(n-1):
            if arr[i][j]==0:
                if j==0 and arr[i][j]==0:
                    arr[i][j]=1
                    newladder(i, j, 1, k)
                    arr[i][j]=0
                elif j==n-2 and arr[i][j-1]==0:
                    arr[i][j]=1
                    newladder(i, j, 1, k)
                    arr[i][j]=0
                elif 0<j<n-2 and arr[i][j]==0 and arr[i][j-1]==0:
                    arr[i][j]=1
                    newladder(i, j, 1, k)
                    arr[i][j]=0
print(answer if answer<1e9 else -1)