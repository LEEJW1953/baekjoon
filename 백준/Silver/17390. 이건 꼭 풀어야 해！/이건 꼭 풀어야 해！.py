import sys
input=sys.stdin.readline

n, q = map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()
arr1=[0]
for i in range(n):
    arr1.append(arr[i]+arr1[i])
for _ in range(q):
    x, y = map(int, input().split())
    print(arr1[y]-arr1[x-1])