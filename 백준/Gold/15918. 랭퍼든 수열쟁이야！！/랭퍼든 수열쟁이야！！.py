import sys
input=sys.stdin.readline

def dfs(d):
    global count, tmp
    if d==tmp:
        dfs(d+1)
    if d==n+1:
        count+=1
        return
    for i in range(1, 2*n-d):
        if arr[i]==0 and arr[i+d+1]==0:
            arr[i]=d
            arr[i+d+1]=d
            dfs(d+1)
            arr[i]=0
            arr[i+d+1]=0
    return

n, x, y = map(int, input().split())
count=0
arr=[0]*(2*n+1)
tmp=y-x-1
arr[x]=tmp
arr[y]=tmp
dfs(1)
print(count)