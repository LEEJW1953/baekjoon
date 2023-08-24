import sys
input=sys.stdin.readline

n=int(input())
arr=[input().strip() for _ in range(n)]
asc=arr[:]
asc.sort()
isAsc, isDes = True, True
for i in range(n):
    if asc[i]!=arr[i]:
        isAsc=False
    if asc[i]!=arr[n-1-i]:
        isDes=False
if isAsc:
    print('INCREASING')
elif isDes:
    print('DECREASING')
else:
    print('NEITHER')