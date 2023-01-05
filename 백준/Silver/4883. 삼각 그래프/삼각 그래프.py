import sys
input=sys.stdin.readline

count=0
while True:
    count+=1
    n=int(input())
    g=[]
    arr=[[1e9]*3 for _ in range(n)]
    if n==0:
        break
    for i in range(n):
        g.append(list(map(int, input().split())))
    arr[0][1]=g[0][1]
    arr[0][2]=g[0][1]+g[0][2]
    for y in range(1, n):
        for x in range(3):
            if x==0:
                arr[y][0]=min(arr[y-1][0], arr[y-1][1])+g[y][0]
            elif x==1:
                arr[y][1]=min(arr[y-1][0], arr[y-1][1], arr[y-1][2], arr[y][0])+g[y][1]
            else:
                arr[y][2]=min(arr[y-1][2], arr[y-1][1], arr[y][1])+g[y][2]
    print(f'{count}. {arr[n-1][1]}')