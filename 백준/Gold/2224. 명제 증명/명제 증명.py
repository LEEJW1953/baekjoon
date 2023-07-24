import sys
input=sys.stdin.readline

n=int(input())
INF=int(1e9)
g=[[INF]*58 for _ in range(58)]
count=0
for _ in range(n):
    s=input().split()
    start, end = ord(s[0])-65, ord(s[2])-65
    g[start][end]=1
for k in range(58):
    for i in range(58):
        for j in range(58):
            g[i][j]=min(g[i][j], g[i][k]+g[k][j])
for i in range(58):
    for j in range(58):
        if g[i][j]!=INF and i!=j:
            count+=1
print(count)
for i in range(58):
    for j in range(58):
        if g[i][j]!=INF and i!=j:
            print(f'{chr(i+65)} => {chr(j+65)}')