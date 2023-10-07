import sys
input=sys.stdin.readline

def count(tmp):
    if g[i-1][j-1]=='J':
        tmp[0]+=1
    if g[i-1][j-1]=='O':
        tmp[1]+=1
    if g[i-1][j-1]=='I':
        tmp[2]+=1
    return tmp

m, n = map(int, input().split())
k=int(input())
g=[list(input().strip()) for _ in range(m)]
arr=[[[0, 0, 0] for _ in range(n+1)]]
for i in range(1, m+1):
    tmp=[[0, 0, 0]]
    for j in range(1, n+1):
        cur=count(tmp[j-1][:])
        cur[0]+=arr[i-1][j][0]-arr[i-1][j-1][0]
        cur[1]+=arr[i-1][j][1]-arr[i-1][j-1][1]
        cur[2]+=arr[i-1][j][2]-arr[i-1][j-1][2]
        tmp.append(cur)
    arr.append(tmp)
for _ in range(k):
    a,b,c,d=map(int, input().split())
    [j, o, i]=[arr[c][d][i]-arr[c][b-1][i]-arr[a-1][d][i]+arr[a-1][b-1][i] for i in range(3)]
    print(j, o, i)