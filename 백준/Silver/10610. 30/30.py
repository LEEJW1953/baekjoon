import sys
input=sys.stdin.readline

arr=list(map(int, input().strip()))
if sum(arr)%3!=0 or (0 not in arr):
    print(-1)
else:
    print(''.join(sorted(list(map(str, arr)), reverse=True)))