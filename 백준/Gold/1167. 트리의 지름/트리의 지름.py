import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v, dis, vis):
    global res, V
    if dis>res:
        res=dis
        V=v
    for i in range(len(g[v])):
        if not vis[g[v][i][0]]:
            vis[g[v][i][0]]=1
            dfs(g[v][i][0], dis+g[v][i][1], vis)
            vis[g[v][i][0]]=0

v=int(input())
g=[[] for _ in range(v+1)]
for _ in range(v):
    arr=list(map(int, input().split()))
    tmp=[]
    for i in range(1, len(arr)-1, 2):
        tmp.append([arr[i], arr[i+1]])
    g[arr[0]]=tmp
res, V =0, 1
vis=[0]*(v+1)
vis[V]=1
dfs(V, 0, vis)
res=0
vis=[0]*(v+1)
vis[V]=1
dfs(V, 0, vis)
print(res)