import sys
input=sys.stdin.readline

arr=[list(map(int, input().split())) for _ in range(9)]
res=0
x, y=1, 1
for i in range(9):
    for j in range(9):
        if arr[i][j]>res:
            res=arr[i][j]
            x=i+1
            y=j+1
print(res)
print(x, y)