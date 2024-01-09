import sys
input=sys.stdin.readline

def visit(x):
    for i in range(5):
        for j in range(5):
            if g[i][j]==x:
                vis[i][j]=1
                return

def check():
    count, diag1, diag2 = 0, 0, 0
    for i in range(5):
        tmp=0
        for j in range(5):
            if vis[j][i]:
                tmp+=1
        if tmp==5:
            count+=1
        if sum(vis[i])==5:
            count+=1
    for i in range(5):
        if vis[4-i][i]:
            diag1+=1
        if vis[i][i]:
            diag2+=1
    if diag1==5:
        count+=1
    if diag2==5:
        count+=1
    return count>=3

g=[list(map(int, input().split())) for _ in range(5)]
vis=[[0]*5 for _ in range(5)]
ans=0
res=0
for i in range(5):
    arr=list(map(int, input().split()))
    for j in arr:
        visit(j)
        res+=1
        if not ans and check():
            ans=res
print(ans)