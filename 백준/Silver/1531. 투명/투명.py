import sys
input=sys.stdin.readline

def hide(x1, y1, x2, y2):
    for j in range(y1-1, y2):
        for k in range(x1-1, x2):
            arr[j][k]+=1

n, m = map(int, input().split())
arr=[[0]*100 for _ in range(100)]
count=0
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    hide(x1, y1, x2, y2)
for i in range(100):
    for j in range(100):
        if arr[i][j]>m:
            count+=1
print(count)