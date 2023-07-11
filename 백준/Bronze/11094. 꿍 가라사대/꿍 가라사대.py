import sys
input=sys.stdin.readline

n=int(input())
for i in range(n):
    s=input().strip()
    arr=s.split()
    if len(arr)>2:
        if arr[0]=='Simon' and arr[1]=='says':
            print('',' '.join(arr[2:]))