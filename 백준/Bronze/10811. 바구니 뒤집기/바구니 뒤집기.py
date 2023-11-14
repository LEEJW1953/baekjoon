import sys
input=sys.stdin.readline

n, m = map(int, input().split())
arr=list(range(1, n+1))
for i in range(m):
    a, b = map(int, input().split())
    tmp=arr[a-1:b]
    for j in range(b-a+1):
        arr[b-1-j]=tmp[j]
print(*arr)