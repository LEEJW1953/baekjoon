import sys
input=sys.stdin.readline

r, c = map(int, input().split())
g=[list(map(int, input().split())) for _ in range(r)]
t=int(input())
arr=[]
ans=0
for i in range(r-2):
    for j in range(c-2):
        tmp=[]
        for k in range(i, i+3):
            for l in range(j, j+3):
                tmp.append(g[k][l])
        tmp.sort()
        arr.append(tmp[4])
for i in arr:
    if i>=t:
        ans+=1
print(ans)