import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
arr=list(map(int, input().split()))
maxx = 0
for i in range(1,m):
    maxx = max(maxx, arr[i] - arr[i-1])

print(max((maxx+1)//2,arr[0] - 0, n - arr[-1]))