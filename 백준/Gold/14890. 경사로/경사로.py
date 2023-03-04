import sys
input=sys.stdin.readline

def slope(arr):
    global answer
    k=len(arr)
    vis=[0]*k
    for i in range(1, n):
        if arr[i-1]==arr[i] or vis[i]:
            continue
        if abs(arr[i-1]-arr[i])>1:
            return
        if arr[i-1]==arr[i]-1 and i>=l:
            tmp=True
            for j in range(l):
                if vis[i-1-j] or arr[i-1]!=arr[i-1-j]:
                    return
            if tmp:
                for j in range(l):
                    vis[i-1-j]=1
        elif arr[i-1]==arr[i]+1 and i<=n-l:
            tmp=True
            for j in range(l):
                if vis[i+j] or arr[i]!=arr[i+j]:
                    return
            if tmp:
                for j in range(l):
                    vis[i+j]=1
        else:
            return
    answer+=1
    return


n, l = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
answer=0
for i in range(n):
    slope(g[i])
for i in range(n):
    tmp=[]
    for j in range(n):
        tmp.append(g[j][i])
    slope(tmp)
print(answer)