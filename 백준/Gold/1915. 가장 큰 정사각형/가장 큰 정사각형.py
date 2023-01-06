import sys
input=sys.stdin.readline

n, m=map(int, input().split())
arr=[]
res=0
for i in range(n):
    arr1=[]
    for j in input().strip():
        arr1.append(int(j))
    arr.append(arr1)
for i in range(n):
    for j in range(m):
        if 0<i and 0<j:
            if arr[i][j]!=0:
                arr[i][j]+=min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])
        res=max(res, arr[i][j])
print(res**2)