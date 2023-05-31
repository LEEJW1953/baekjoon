import sys
input=sys.stdin.readline

n, m = map(int, input().split())
arr=[list(input().strip()) for _ in range(n)]
for i in range(n):
    print(''.join(arr[i][::-1]))