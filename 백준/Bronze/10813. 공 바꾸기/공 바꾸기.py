import sys
input=sys.stdin.readline

n, m = map(int, input().split())
arr=list(range(1, n+1))
for _ in range(m):
    i, j = map(int, input().split())
    a, b = arr[i-1], arr[j-1]
    arr[i-1]=b
    arr[j-1]=a
print(*arr)