import sys
input=sys.stdin.readline

n, k = map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
ans=1
cur=[0,0,0,0]
arr.sort(key=lambda x:(-x[1], -x[2], -x[3]))
for i in range(n):
    if arr[i][0]==k:
        target=arr[i][1:]
        break
for i in range(n):
    tmp=arr[i][1:]
    if tmp==target:
        print(i+1)
        break